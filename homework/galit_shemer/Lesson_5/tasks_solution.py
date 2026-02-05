person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person


def extract_and_add_10(result):
    colon_index = result.index(':') + 1
    number_str = result[colon_index:].strip()
    number = int(number_str)
    return number + 10


result_1 = "результат операции: 42"
result_2 = "результат операции: 514"
result_3 = "результат работы программы: 9"

line_1 = 'результат операции: 42'
line_2 = 'результат операции: 514'
line_3 = 'результат работы программы: 9'

index_1 = line_1.index(':') + 2
index_2 = line_2.index(':') + 2
index_3 = line_3.index(':') + 2

print(int(line_1[index_1:]) + 10)
print(int(line_2[index_2:]) + 10)
print(int(line_3[index_3:]) + 10)


students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print(
    f"Students {', '.join(students)} study these subjects: {', '.join(subjects)}"
)
