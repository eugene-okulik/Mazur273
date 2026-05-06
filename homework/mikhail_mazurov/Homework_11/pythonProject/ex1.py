class Book:
    page_material = 'бумага'
    with_text = True
    is_reserved = False

    def __init__(self, title, author, page_numbers, ISBN):
        self.title = title
        self.author = author
        self.page_numbers = page_numbers
        self.ISBN = ISBN


book1 = Book('Тестирование dot com', 'Майерс', 500, '001')
book2 = Book('The art of software testing', 'Назина', 50, '002')
book3 = Book('Тестирование программного обеспечения', 'Савин', 5, '003')
book4 = Book('Автоматизация тестирования на Python', 'Окулик', 500, '004')
book5 = Book('Что такое тестирование', 'Куликов', 50, '005')


book4.is_reserved = True

books = [book1, book2, book3, book4, book5]

for book in books:
    if book.is_reserved:
        print(f'Название: {book.title}, Автор: {book.author}, страниц: {book.page_numbers}, '
              f'материал: {Book.page_material}, зарезервирована')
    else:
        print(f'Название: {book.title}, Автор: {book.author}, страниц: {book.page_numbers}, '
              f'материал: {Book.page_material}')


class SchoolBooks(Book):
    with_exercise = True
    def __init__(self, title, author, page_numbers, ISBN, subject, group):
        super().__init__(title, author, page_numbers, ISBN)
        self.subject = subject
        self.group = group


book6 = SchoolBooks('Цветок и нож', 'ВИАГра', 100, "006", "Биология", "18+")
book7 = SchoolBooks('3 полоски', 'AnimalJazz', 20, "007", "Математика", "9")
book8 = SchoolBooks('Moscow', 'Rammstain', 100, "008", "География", "5")
book9 = SchoolBooks(
    'Миллион алых роз', 'Пугачева', 1000000, "009", "Экономика", "9"
)
book10 = SchoolBooks('18 мне уже', 'Руки Вверх', 5, "010", "УК РФ", "11")

book9.is_reserved = True

schoolbook = [book6, book7, book8, book9, book10]

for x in schoolbook:
    if x.is_reserved:
        print(f'Название: {x.title}, Автор: {x.author}, страниц: {x.page_numbers}, '
              f'Предмет: {x.subject}, Класс: {x.group}, зарезервирована')
    else:
        print(f'Название: {x.title}, Автор: {x.author}, страниц: {x.page_numbers}, '
              f'Предмет: {x.subject}, Класс: {x.group}')
