import os
from datetime import datetime, timedelta


base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "test_data.txt")


with open(file_path, encoding="utf-8") as data_file:
    for line in data_file:
        parts = line.strip().split(" - ")

        number_and_date = parts[0]
        action = parts[1]

        date_string = number_and_date.split(". ", 1)[1]
        date = datetime.strptime(
            date_string,
            "%Y-%m-%d %H:%M:%S.%f"
        )

        if line.startswith("1."):
            print(date + timedelta(weeks=1))

        elif line.startswith("2."):
            print(date.strftime("%A"))

        elif line.startswith("3."):
            days_ago = datetime.now() - date
            print(days_ago.days)
