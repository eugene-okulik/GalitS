from functools import wraps


def finish_me(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("finished")
        return result

    return wrapper


def repeat_me(func=None, *, count=1):
    if func is None:

        def decorator(inner_func):

            @wraps(inner_func)
            def wrapper(*args, **kwargs):
                for _ in range(count):
                    inner_func(*args, **kwargs)

            return wrapper

        return decorator

    @wraps(func)
    def wrapper(*args, **kwargs):
        times = kwargs.pop("count", count)
        for _ in range(times):
            func(*args, **kwargs)

    return wrapper
