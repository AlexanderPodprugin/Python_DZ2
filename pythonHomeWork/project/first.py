# -*- coding: windows-1251 -*

def get_reg(reg):
    if "����" in reg.lower():
        schedule()

    elif "������" in reg.lower():
        training()

    elif "����" in reg.lower():
        contact()

    elif "����" in reg.lower():
        price()

    elif "�������" in reg.lower():
        coaches()

def schedule():
    print("�� - 17:00-21:00, �� - 17:00-21:00, �� - 16:30-19:30")


def price():
    print("����� �������: 3000")


def training():
    print("�����������: ������� ����������, ��������")


def contact():
    print("��������: +79888887465")


def coaches():
    print("�������: ������� ��������, ���� ������, ������� ��������")