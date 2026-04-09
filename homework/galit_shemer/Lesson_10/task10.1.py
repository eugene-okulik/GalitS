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


def operation_control(func):
    @wraps(func)
    def wrapper(first, second):
        if first == second:
            return func(first, second, "+")
        if first < 0 or second < 0:
            return func(first, second, "*")
        if first > second:
            return func(first, second, "-")
        return func(first, second, "/")

    return wrapper


@operation_control
def calc(first, second, operation):
    if operation == "+":
        return first + second
    if operation == "-":
        return first - second
    if operation == "*":
        return first * second
    if operation == "/":
        return first / second


PRICE_LIST = """тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р"""


price_dict = {
    item.split()[0]: int(item.split()[1][:-1])
    for item in PRICE_LIST.split("\n")
}


@finish_me
def example(text):
    print(text)


@repeat_me
def example_repeat(text):
    print(text)


@repeat_me(count=2)
def example_repeat2(text):
    print(text)


if __name__ == "__main__":
    example("print me")

    example_repeat("print me", count=2)

    example_repeat2("print me")

    print(calc(5, 5))
    print(calc(10, 5))
    print(calc(5, 10))
    print(calc(-2, 3))

    print(price_dict)