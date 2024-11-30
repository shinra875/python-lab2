import csv

mass = []

with open('books-en.csv', 'r', encoding='cp1251') as f:  # Открываем CSV файл с нужной кодировкой
    reader = csv.reader(f, delimiter=';')  # Устанавливаем разделитель
    
    header = next(reader)  # Читаем заголовок
    print('Headers: ', header)  # Вывод заголовков
    
    for row in reader:
        # Проверяем, что в строке ровно 7 элементов
        if len(row) == 7:
            mass.append(row)
        else:
            print(f"Строка пропущена из-за некорректного количества элементов: {row}")  # Некоторые ячейки имеют в себе знак разделителя, что существенно усложняет работы. будем пропускать такие строки, ведь строк с рейтингом 25 очень много, так что эти пропуски никак не повлияют на итоговый результат


sorted_books = []  # Создаём список для хранения отсортированных книг

for book in mass:  # Формируем список списков и добавляем информацию о рейтинге
    rating = book[5]  # Рейтинг книги (предпоследний элемент)
    sorted_books.append((book, rating))  # Сохраняем книгу вместе с её рейтингом

sorted_books.sort(key=lambda x: float(x[1]), reverse=True)  # Сортируем по рейтингу (по убыванию)

k=0
for book, rating in sorted_books:  # Выводим отсортированные списки
    k+=1
    print(f"{k}, Количество элементов: {len(book)}, Рейтинг: {rating}, Данные: {book}")
    if k == 20:
        break