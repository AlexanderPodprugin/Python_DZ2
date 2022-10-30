def generator2(t):
    buffer = t.split(' ')
    for j in buffer:
        if j.find('\n') != -1:
            yield j
        else:
            yield j



def main():
    a = generator2("√енератор Ц это итератор, элементы которого можно перебирать (итерировать) только один раз. "
                   "»тератор Ц это объект, который поддерживает функцию next()дл€ перехода к следующему элементу коллекции.")
    for el in a:
        print(el)


main()