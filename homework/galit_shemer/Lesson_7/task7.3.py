def extract_and_add_10(text):
    number = int(text.split(":")[-1].strip())
    return number + 10


results = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2",
]


for item in results:
    print(extract_and_add_10(item))
