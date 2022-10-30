# -*- coding: windows-1251 -*

def get_reg(reg):
    if "расп" in reg.lower():
        schedule()

    elif "направ" in reg.lower():
        training()

    elif "конт" in reg.lower():
        contact()

    elif "плат" in reg.lower():
        price()

    elif "тренеры" in reg.lower():
        coaches()

def schedule():
    print("Пн - 17:00-21:00, Вт - 17:00-21:00, Ср - 16:30-19:30")


def price():
    print("Ценна занятий: 3000")


def training():
    print("Направления: Силовая тренировка, Растяжка")


def contact():
    print("Контакты: +79888887465")


def coaches():
    print("Тренеры: Виталий Алексеев, Иван Иванов, Дмитрий Степанов")