import csv

search_author = input('Введите автора, чьи книги хотите найти: ')

with open('books-en.csv', 'r', encoding='cp1251') as f:
    reader = csv.reader(f, delimiter=';')  # Указываем разделитель
    
    header = next(reader)
    print('Headers: ', header)
    
    for row in reader:
        # Проверяем, что строка содержит нужное количество элементов
        if len(row) < 5:
            continue
        
        year = row[3]  # Предполагаем, что год находится в 4-й колонке
        author = row[2]  # Предполагаем, что автор находится в 3-й колонке

        # Пробуем преобразовать год в число
        try:
            year = int(year)
        except ValueError:
            continue  # Если не удалось преобразовать, пропускаем эту строку

        # Проверяем, если автор совпадает с искомым
        authors_list = [a.strip() for a in author.split(';')]  # Разделяем авторов и убираем лишние пробелы

        if year >= 2000 and search_author in authors_list:
            print(row)
