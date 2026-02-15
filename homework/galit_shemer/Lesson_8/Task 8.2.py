import sys


sys.set_int_max_str_digits(0)


def fibonacci_generator():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def main():
    targets = {5, 200, 1000, 100000}
    results = {}

    for index, value in enumerate(fibonacci_generator(), start=1):
        if index in targets:
            results[index] = value
            if len(results) == len(targets):
                break

    print(results[5])
    print(results[200])
    print(results[1000])
    print(results[100000])


if __name__ == "__main__":
    main()
