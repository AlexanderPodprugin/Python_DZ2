def F5(_colors,_count):
    dictionary = {}
    for i in range(count):
        key = input('¬ведите цвет')
        value = input('¬ведите его HEX-значение')
        dictionary[key] = value
    return(dictionary)

colors = '÷вета'
count = int(input('¬ведите количество цветов: '))
print(F5(colors,count))