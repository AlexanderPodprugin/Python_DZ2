def discount(_score):
    if (_score >= 0) and (_score <= 49):
        print('���� ������: 10%')
        return True
    elif (_score >= 50) and (_score <= 99):
        print('���� ������: 15%')
        return True
    elif (_score >= 100):
        print('���� ������: 10%')
        return True
    else:
        print('���������� ������ �� ����� ���� ������������� ������.')
        return False

flag = False
while (flag == False):
    score = int(input('������� ���������� ������: '))
    flag = discount((score))