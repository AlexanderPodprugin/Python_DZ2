name = input('������� ��� ��� (off - �����): ')
while (name.lower() != 'off'):
     answer = lambda _name : _name + ' - �����'
     print(answer(name))
     name = input('������� ��� ��� (off - �����): ')