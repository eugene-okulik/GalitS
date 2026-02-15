person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

def extract_and_add_10(result):
    number = int(result.split(':')[-1].strip())
    return number + 10

results = [
    'результат операции: 42',
    'результат операции: 514',
    'результат работы программы: 9'
]

for r in results:
    print(extract_and_add_10(r))

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print(f"Students {', '.join(students)} study these subjects: {', '.join(subjects)}")
