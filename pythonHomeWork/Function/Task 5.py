def imt(_weight,_height):
    _index = _weight/(_height**2)
    return _index

def imt_analyse(_index_analyse):
    if (_index_analyse < 18.5):
        print('������������� ���')
    elif (_index_analyse >= 18.5) and (_index_analyse <= 25):
        print('��� � �����')
    else:
        print('���������� ���')

weight = int(input('������� ��� ���: '))
height = int(input('������� ��� ����:' ))
while (weight <= 0):
    print('��� �� ����� ���� �������������.')
    weight = int(input('������� ��� ���: '))
while (height <= 0):
    print('���� �� ����� ���� �������������.')
    height = int(input('������� ��� ����: '))
index = imt(weight,height)
imt_analyse(index)