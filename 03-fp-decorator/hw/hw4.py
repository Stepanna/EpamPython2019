from functools import wraps
import time
import urllib.request


def make_cache(maxtime):
    """
    The max-age request directive defines (sec) the amount of time it takes
     for a cached copy of a resource to expire. After expiring, a browser must
     refresh its version of the resource by sending another request to a server
    """
    storage = {}

    def inner_func(function):
        @wraps(function)
        def wrapper(*args):
            if args in storage:
                result, timestamp = storage[args]
                age = time.time() - timestamp
                if age >= maxtime:
                    del(storage[args])
            else:
                result = function(*args)
                storage[args] = (result, time.time())
            return result
        return wrapper
    return inner_func


@make_cache(100)
def slow_function(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()
    return html


slow_function('http://python.org/')
