def task1(l):
    for el in l:
        try:
            print(el / 3)
        except TypeError as e:
            print('���������� ���������')


lst = ["������",12,14,"����","100"]
task1(lst)