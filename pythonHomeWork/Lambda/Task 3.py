symbols_one = ['�','�','�','�']
symbols_two = ['�','�','�','�']
name = input('������� ��� ��� (off - �����): ')
while (name.lower() != 'off'):
    if (name.upper()[-1] in symbols_one):
       a = lambda _name : _name + ' - �����'
       print(a(name))
    elif (name.upper()[-1] in symbols_two):
        b = lambda _name : _name + ' - ����������'
        print(b(name))
    else:
        c = lambda  _name : '������ ' +  _name
        print(c(name))
    name = input('������� ��� ��� (off - �����): ')