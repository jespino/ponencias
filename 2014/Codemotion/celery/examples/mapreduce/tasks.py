from celery import Celery, group, chain, chord
import requests
from bs4 import BeautifulSoup


app = Celery('tasks', backend='amqp', broker='amqp://guest@localhost//')

@app.task
def fetch_url(url):
    response = requests.get(url)
    return response.text

@app.task
def get_links(contents):
    result = []
    for content in contents:
        soap = BeautifulSoup(content)
        for a in soap.find_all("a"):
            result.append(a.get('href'))
    return result

@app.task
def join(data):
    return "\n".join(data)

if __name__ == "__main__":
    urls = [
        "http://www.google.com",
        "http://www.facebook.com",
        "http://www.github.com",
        "http://www.yahoo.com",
    ]
    res = chord([fetch_url.s(url) for url in urls], get_links.s() | join.s())()
    print(res.get())
