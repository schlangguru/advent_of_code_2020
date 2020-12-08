import time

def benchmark(func):
    """
    Decorator for func that measures the time the function takes.
    """
    def decorated(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        millis = (end - start) * 1000
        print(f"{func.__name__} took {millis:.2f} ms")

        return result

    return decorated