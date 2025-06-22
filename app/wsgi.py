"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.contrib.auth import get_user_model
from django.db.utils import OperationalError
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')


FIXTURES = [
    'goods/fixtures/categories.json',
    'goods/fixtures/products.json',
]

INIT_FLAG = os.path.join(os.path.dirname(__file__), '.initialized')
if not os.path.exists(INIT_FLAG):
    try:
        # 1. Выполняем миграции
        from django.core.management import execute_from_command_line
        execute_from_command_line(['manage.py', 'migrate'])
        
        # 2. Создаем суперпользователя
        User = get_user_model()
        if not User.objects.filter(username='toor').exists():
            User.objects.create_superuser(
                username='toor',
                email='toor@toormail.ru',
                password='hbXE2U3JebaKfeA'
            )
            print("Суперпользователь 'toor' создан")

        for fixture in FIXTURES:
            try:
                if os.path.exists(fixture):
                    call_command('loaddata', fixture)
                    print(f"✅ Загружена фикстура: {fixture}")
                else:
                    print(f"⚠️ Файл фикстуры не найден: {fixture}")
            except Exception as e:
                print(f"⚠️ Ошибка загрузки {fixture}: {str(e)}")

        # 3. Создаем маркер завершения
        open(INIT_FLAG, 'w').close()
        print("Инициализация выполнена")
        
    except OperationalError as e:
        print(f"Ошибка инициализации: {e}")
        # Продолжаем работу, даже если не удалось инициализировать

application = get_wsgi_application()
