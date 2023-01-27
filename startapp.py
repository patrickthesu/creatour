import os

def execStr (command):
    command = ["manage.py",str ( command )]
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'creatour.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(command)

def migrate ():
    execStr ("makemigrations")
    execStr ("migrate")

def main ():
    migrate ()
    execStr ("runserver")
    

if __name__ == "__main__":
    main()


