def sum(n1, n2):
    return n1 + n2

def minus(n1, n2):
    return n1 - n2


def multyply(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2

print('1.sum / 2.minus / 3.multyply / 4.division')
i = int(input('Select the operation you want:'))

n1 = float(input('Enter the number for first number:'))

n2 = float(input('Enter the number for second number:'))

if i == 1:
    print('The sum equal is', sum(n1, n2))
elif i == 2:
    print('The sum equal ', isminus(n1, n2))
elif i == 3:
    print('The sum equal is', multyply(n1, n2))
elif i == 4:
    print('The sum equal ', isdivision(n1, n2))
