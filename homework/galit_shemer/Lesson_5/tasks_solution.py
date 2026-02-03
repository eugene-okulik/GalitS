person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

print(name)
print(last_name)
print(city)
print(phone)
print(country)


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
