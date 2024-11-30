import csv

k_task1 = 0
with open('books-en.csv', 'r', encoding='cp1251') as f:
    reader = csv.reader(f)
    
    header = next(reader)
    print('Headers: ', header)
    
    for row in reader:
        # row содержит одну строку, нужно разбить её на элементы
        elements = row[0].split(';')  # Разбиваем строку на элементы
        book_title = elements[1]  # Получаем название книги (второй элемент)
        
        l = len(book_title)
        if l > 30:
            k_task1 += 1
            print(f'{k_task1}, Длина названия = {l}, {elements}')  # Выводим номер, длину и элементы строки
print('Ответ на первое задание: ', k_task1)
