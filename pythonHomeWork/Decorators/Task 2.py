def decorate(eat):
    def wrapper():
        print("�������� ������� �������.")
        eat()
        print("������� ���� �� ��� ����.")
        print("�������� ��� ���������.")
    return wrapper
@decorate
def eat_to_decor():
    print("��� ������������ ��������� �������� ���: ������ � �����!")

eat_to_decor()