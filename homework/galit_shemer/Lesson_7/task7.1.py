secret_number = 7

while True:
    guess = int(input("Угадайте число: "))
    if guess == secret_number:
        print("Поздравляю! Вы угадали!")
        break
    else:
        print("Попробуйте снова")
