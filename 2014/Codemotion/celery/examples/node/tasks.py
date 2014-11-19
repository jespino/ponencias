from celery import Celery, group, chain, chord
import time

app = Celery('tasks', backend='amqp', broker='amqp://guest@localhost//')

class Config:
    CELERY_RESULT_SERIALIZER="json"

app.config_from_object(Config)

@app.task
def add(x, y):
    return x + y
