def allowance(_score):
    global flag
    if (_score > 50):
        flag = True
        return True
    elif (_score >= 0) and (_score <= 50):
        flag = True
        return False
    else:
        flag = False

count = int(input('������� ���������� ��������: '))
help_count = 0
flag = False
for i in range(count):
    score = int(input('������� ���������� ������: '))
    answer = allowance(score)
    help_count += 1
    while (flag == False):
        score = int(input('���������� ������ �� ����� ���� ������������� ������, ��������� �������: '))
        answer = allowance(score)
    flag = False
    if (answer == False):
        print(help_count,':',answer, '(�� ���������)')
    else:
        print(help_count,':',answer)