import xml.dom.minidom as x


d = {}
domtree = x.parse('currency.xml')
group = domtree.documentElement


valutes = group.getElementsByTagName('Valute')
print(f'Name - CharCode')
for Valute in valutes:
    
    
    numcode = Valute.getElementsByTagName('NumCode')[0].childNodes[0].nodeValue
    charcode = Valute.getElementsByTagName('CharCode')[0].childNodes[0].nodeValue
    nominal = Valute.getElementsByTagName('Nominal')[0].childNodes[0].nodeValue
    name = Valute.getElementsByTagName('Name')[0].childNodes[0].nodeValue
    value = Valute.getElementsByTagName('Value')[0].childNodes[0].nodeValue
    vunitrate = Valute.getElementsByTagName('VunitRate')[0].childNodes[0].nodeValue
    
    d[1] = name
    d[2] = charcode
    
    # чтобы увидеть блоки со всей информацией для конкретных валют, раскомментируйте следующие 7 строк
    
    # print(f'\n\n-- Valute {Valute.getAttribute('ID')} --')
    # print(f'numcode: {numcode}')
    # print(f'charcode: {charcode}')
    # print(f'nominal: {nominal}')
    # print(f'name: {name}')
    # print(f'value: {value}')
    # print(f'vunitrate: {vunitrate}')
    
    print(f'{d[1]} - {d[2]}')