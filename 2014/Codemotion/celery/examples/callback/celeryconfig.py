from datetime import timedelta
from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    'add-every-3-seconds': {
        'task': 'tasks.add',
        'schedule': timedelta(seconds=3),
        'args': (16, 16)
    },
    'run-it-once-a-week': {
        'task': 'tasks.add',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
        'args': (16, 16)
    },
}

CELERY_TIMEZONE = 'UTC'
