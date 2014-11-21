from celery import Celery, group, chain, chord
import time

app = Celery('tasks', backend='amqp', broker='amqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y

if __name__ == "__main__":
    res = add.apply_async((2, 2), link=add.s(2))
    print(res.get())
