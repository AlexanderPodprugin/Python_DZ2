from time import *

print('������� � ����?')
seconds = int(input('������� ���������� ������ (2 ��� 10): '))
if (seconds == 2) or (seconds == 10):
    print('�� ������� � ���� ��',seconds,'������(-�)')
    sleep(seconds)
    print('������������� �� ����')