class Book:
    def __init__(self, material, has_text, title, author, pages, isbn, reserved=False):
        self.material = material
        self.has_text = has_text
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved

    def print_info(self):
        if self.reserved:
            print(f"Название: {self.title}, Автор: {self.author}, "
                  f"страниц: {self.pages}, материал: {self.material}, зарезервирована")
        else:
            print(f"Название: {self.title}, Автор: {self.author}, "
                  f"страниц: {self.pages}, материал: {self.material}")


class SchoolBook(Book):
    def __init__(self, material, has_text, title, author, pages, isbn,
                 subject, grade, has_tasks, reserved=False):
        super().__init__(material, has_text, title, author, pages, isbn, reserved)
        self.subject = subject
        self.grade = grade
        self.has_tasks = has_tasks

    def print_info(self):
        if self.reserved:
            print(f"Название: {self.title}, Автор: {self.author}, "
                  f"страниц: {self.pages}, предмет: {self.subject}, "
                  f"класс: {self.grade}, зарезервирована")
        else:
            print(f"Название: {self.title}, Автор: {self.author}, "
                  f"страниц: {self.pages}, предмет: {self.subject}, "
                  f"класс: {self.grade}")


# --- книги ---
book1 = Book("бумага", True, "Идиот", "Достоевский", 500, "123")
book2 = Book("бумага", True, "Преступление и наказание", "Достоевский", 400, "124")
book3 = Book("бумага", True, "1984", "Оруэлл", 300, "125")
book4 = Book("бумага", True, "Мастер и Маргарита", "Булгаков", 350, "126")
book5 = Book("бумага", True, "Анна Каренина", "Толстой", 600, "127")

book1.reserved = True

for book in [book1, book2, book3, book4, book5]:
    book.print_info()


# --- учебники ---
sb1 = SchoolBook("бумага", True, "Алгебра", "Иванов", 200, "201",
                 "Математика", 9, True)
sb2 = SchoolBook("бумага", True, "География", "Петров", 180, "202",
                 "География", 8, True)
sb3 = SchoolBook("бумага", True, "История", "Сидоров", 220, "203",
                 "История", 7, False)

sb1.reserved = True

for sb in [sb1, sb2, sb3]:
    sb.print_info()