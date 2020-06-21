#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
sys.path.append('/private/var/mobile/Containers/Shared/AppGroup/BF6D28F7-8CDD-43FE-AAB3-F1369C817B0C/File Provider Storage/Repositories/my-first-blog/mysite/')
sys.path.append('/private/var/mobile/Containers/Shared/AppGroup/63EBE0A2-52DE-41F0-8090-7B3F107FB4B6/File Provider Storage/Repositories/my-first-blog/mysite')


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
