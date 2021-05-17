import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cryptomap.settings')
BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')
app = Celery('cryptomap')
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()
app.conf.broker_url = BASE_REDIS_URL
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'


app.conf.beat_schedule = {
    'add-every-15minute-contrab': {
        'task': 'track_for_discount',
        'schedule': crontab(minute='*/5'),
        'args': (16, 16),
    },
}