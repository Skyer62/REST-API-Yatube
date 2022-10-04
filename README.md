# REST API Yatube
REST API для проекта Yatube
# Стек технологий
- Python + Django REST Framework
- Simple JWT - работа с токеном
- SQLite3 - база данных
- Git - система контроля версий
# Установка
1. Клонирйте репозиторий с проектом
```sh
git clone https://github.com/vadim62/hw05_final
```
2. В созданной директории установите виртуальное окружение, активируйте его и установите необходимые зависимости:
```sh
python -m venv venv

. venv/bin/activate

pip install -r requirements.txt
```
3. Выполните миграции:
```sh
python manage.py api_yamdb migrate
```
4. Запуск проекта:
```sh
python manage.py runserver
```
Проект доступен по адресу: http://127.0.0.1:8000/
