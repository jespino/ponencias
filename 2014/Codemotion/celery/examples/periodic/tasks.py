from celery import Celery, group, chain, chord
import time
import celeryconfig

app = Celery('tasks', backend='amqp', broker='amqp://guest@localhost//')

app.config_from_object(celeryconfig)

@app.task
def add(x, y):
    return x + y

if __name__ == "__main__":
    res = add.apply_async((2, 2))
    print(res.get())
