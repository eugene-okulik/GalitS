import random
import sys

sys.set_int_max_str_digits(0)

salary = int(input("Введите зарплату: "))
bonus = random.choice([True, False])

if bonus:
    salary += random.randint(1, salary)

print(f"{salary}, {bonus} - '${salary}'")


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


targets = {5, 200, 1000, 100000}
results = {}

for i, x in enumerate(fibonacci_generator(), 1):
    if i in targets:
        results[i] = x
        if len(results) == len(targets):
            break

print(results[5])
print(results[200])
print(results[1000])
print(results[100000])
