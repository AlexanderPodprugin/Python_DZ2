from random import randint
from time import *

count1 = 0
count2 = 0
i = input('������� ��� ��������� (off - ��������� ������): ')
while i != 'off':
    number = randint(1,2)
    sleep(1)
    print('��� �����: ',number)
    if (number == 1):
        count1 += 1
    else:
        count2 += 1
    sleep(1)
    print('���������� � ������ ������: ',count1,'. ���������� �� ������ ������: ',count2)
    sleep(1)
    i = input('������� ��� ��������� (off - ��������� ������): ')
sleep(1)
print()
print('���������� � ������ ������: ',count1,'. ���������� �� ������ ������: ',count2)