import csv

k_task3 = 0
mass = []

with open('books-en.csv', 'r', encoding='cp1251') as f:
    reader = csv.reader(f, delimiter=';')
    
    header = next(reader)
    print('Headers: ', header)
    
    for row in reader:
        k_task3+=1
        
        author = row[2]
        title = row[1]
        year = row[3]
        
        try:
            year = int(year)
        except ValueError:
            continue  # Если не удалось преобразовать, пропускаем эту строку
        
        mass.append(f'{k_task3}. {author}. {title} - {year}')
        
        if k_task3 == 20:
            break


print(mass, end='\n\n')
for i in range(len(mass)):
    print(mass[i])