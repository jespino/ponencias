from celery import Celery, group, chain, chord
import time

app = Celery('tasks', backend='amqp', broker='amqp://guest@localhost//')

@app.task
def fetch_url(url):
    return "CONTENT DATA"

@app.task
def lowcase(content):
    return content.lower()

@app.task
def split(content):
    return content.split()

@app.task
def flat(data):
    return [item for sublist in data for item in sublist]

@app.task
def sleeper(data):
    time.sleep(1)
    return data

@app.task
def join(data):
    return "#".join(data)

if __name__ == "__main__":
    res = chord([chain(fetch_url.s(url), lowcase.s(), split.s()) for url in ["www.google.com", "www.facebook.com"]], flat.s() | sleeper.s() | join.s())()
    print(res.get())
