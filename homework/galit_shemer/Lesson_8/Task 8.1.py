import random


def main():
    base_salary = int(input("Введите зарплату: "))
    bonus = random.choice([True, False])

    final_salary = base_salary
    if bonus:
        final_salary += random.randint(1, base_salary)

    print(f"{base_salary}, {bonus} - '${final_salary}'")


if __name__ == "__main__":
    main()
