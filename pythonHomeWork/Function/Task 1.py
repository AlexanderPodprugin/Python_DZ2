def bad(_name,_group):
    print('"������� ������"')
    print('���:',_name)
    print('������',_group)

count = int(input('������� ���������� ��������:'))
for i in range(count):
    name = input('������� ���: ')
    group = input('������� ������: ')
    bad(name,group)