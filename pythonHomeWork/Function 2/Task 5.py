def F5(_colors,_count):
    dictionary = {}
    for i in range(count):
        key = input('������� ����')
        value = input('������� ��� HEX-��������')
        dictionary[key] = value
    return(dictionary)

colors = '�����'
count = int(input('������� ���������� ������: '))
print(F5(colors,count))