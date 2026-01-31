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

print(extract_and_add_10(result_1))
print(extract_and_add_10(result_2))
print(extract_and_add_10(result_3))

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
students_text = ', '.join(students)
subjects_text = ', '.join(subjects)
print(f"Students {students_text} study these subjects: {subjects_text}")
