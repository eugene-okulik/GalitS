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
        times = kwargs.pop("count", 1)
        for _ in range(times):
            func(*args, **kwargs)
    return wrapper


def operation_control(func):
    @wraps(func)
    def wrapper(first, second):
        if first == second:
            op = "+"
        elif first < 0 or second < 0:
            op = "*"
        elif first > second:
            op = "-"
        else:
            op = "/"
        return func(first, second, op)
    return wrapper


@finish_me
def example_finish(text):
    print(text)


@repeat_me
def example_repeat(text):
    print(text)


@repeat_me(count=2)
def example_repeat_param(text):
    print(text)


@operation_control
def calc(first, second, operation):
    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "*":
        return first * second
    elif operation == "/":
        return first / second


example_finish("print me")
example_repeat("print me", count=2)
example_repeat_param("print me")

a = float(input())
b = float(input())
print(calc(a, b))

PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price_dict = {
    item.split()[0]: int(item.split()[1].replace("р", ""))
    for item in PRICE_LIST.splitlines()
}

print(price_dict)
