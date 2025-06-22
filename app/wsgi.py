"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')





# Проверка выполнения миграций
MIGRATE_FLAG = os.path.join(os.path.dirname(__file__), '.migrated')
if not os.path.exists(MIGRATE_FLAG):
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage.py', 'migrate'])
    open(MIGRATE_FLAG, 'w').close()

application = get_wsgi_application()