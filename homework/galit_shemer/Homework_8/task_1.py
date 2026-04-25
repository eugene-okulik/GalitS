import random


salary = int(input("Enter salary: "))
bonus = random.choice([True, False])

total_salary = salary
if bonus:
    total_salary += random.randint(1, salary)

print(f"{salary}, {bonus} - ${total_salary}")
