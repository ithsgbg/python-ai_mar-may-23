import requests
from mar15.timeit import time_it

def cache(func):
    saved = {}
    def wrapper(url):
        if url in saved:
            return saved[url]
        result = func(url)
        saved[url] = result
        return result
    return wrapper

@time_it
def web_lookup(url, cache={}):
    if url in cache:
        return cache[url]
    result = requests.get(url).text
    cache[url] = result
    return result

@time_it
@cache
def web_lookup2(url):
    return requests.get(url).text


web_lookup2('http://cnn.com')
web_lookup2('http://cnn.com')
web_lookup2('http://cnn.com')
web_lookup2('http://cnn.com')
web_lookup2('http://cnn.com')
web_lookup2('http://cnn.com')