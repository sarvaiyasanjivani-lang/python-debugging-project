from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function:", func.__name__)
        print("Arguments:", args)
        result = func(*args, **kwargs)
        print("Result:", result)
        return result
    return wrapper

@debug
def multiply(a, b):
    return a * b

multiply(5, 6)
