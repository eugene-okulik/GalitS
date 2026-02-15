

def process_result_line(line):

    parts = line.split()
    number = int(parts[-1])
    return number + 10


lines = [

    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]


for line in lines:
    result = process_result_line(line)
    print(result)
