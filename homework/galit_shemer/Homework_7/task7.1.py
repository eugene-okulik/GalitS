secret_number = 7

guess = None

while guess != secret_number:
    guess = int(input("Угадай число: "))

    if guess != secret_number:
        print("Попробуйте снова")

print("Поздравляю! Вы угадали!")
