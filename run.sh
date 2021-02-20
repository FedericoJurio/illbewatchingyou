celery -A task worker --beat --schedule=task --loglevel=INFO -n 1
