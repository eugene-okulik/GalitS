import sys

sys.set_int_max_str_digits(0)


def fibonacci():
    first, second = 0, 1
    while True:
        first, second = second, first + second
        yield first


for index, number in enumerate(fibonacci(), start=1):
    if index in (5, 200, 1000, 100000):
        print(number)

    if index == 100000:
        break
