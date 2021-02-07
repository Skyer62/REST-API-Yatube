from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import constraints
from django.db.models.constraints import UniqueConstraint

User = get_user_model()


class Post(models.Model):
    text = models.TextField(verbose_name='Текст записи',
                            help_text='Введите текст публикации')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='posts', verbose_name='Автор')
    group = models.ForeignKey('Group', on_delete=models.SET_NULL,
                              blank=True, null=True, related_name='posts',
                              verbose_name='Группа',
                              help_text='Введите название группы')

    def __str__(self):
        return self.text


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=True, related_name='comments')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name='comments')
    text = models.TextField(
        help_text='Введите текст комментария', verbose_name='Текст', max_length=300)
    created = models.DateTimeField('Дата публикации', auto_now_add=True)


class Group(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, verbose_name='Название группы')
    slug = models.SlugField(null=False,
                            verbose_name='Ссылка группы')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title


class Follow(models.Model):
    user = models.ForeignKey(
        User, verbose_name='Подписчик', on_delete=models.CASCADE,
        related_name='follower')
    following = models.ForeignKey(
        User, verbose_name='Автор', on_delete=models.CASCADE,
        related_name='following')

    class Meta:
        constraints = [UniqueConstraint(fields=['user', 'following'],
                                        name='unique_following')]

    def __str__(self):
        return f'{self.user} подписан на {self.following}'
