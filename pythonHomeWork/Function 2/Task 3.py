def F3():
    sum = 0
    num = input('¬ведите число: ')
    if (num != ''):
        sum += int(num) + F3()
        return sum
    else:
        return sum

number = input('¬ведите число: ')
if (number == ''):
    print(0.0)
else:
    print(F3() + int(number))