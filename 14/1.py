from math import sqrt
def work(a,b,c):
    p = (a+b+c)/2
    print('Площадь треугольника: ',sqrt(p*((p-a)*(p-b)*(p-c))))

def is_right(a):
    try:
        a = float(a)
    except ValueError:
        return False
    return a
 
def main():
    while True:
        a = input('Введите a ')
        a = is_right(a)
        if(a is False):
            print('Введите корректное число')
            continue

        b = input('Введите b ')
        b = is_right(b)
        if(b is False):
            print('Введите корректное число')
            continue

        c = input('Введите c ')
        c = is_right(c)
        if(c is False):
            print('Введите корректное число')
            continue

        work(a,b,c)
        asnwer = input("Продолжить? (да/нет) ")
        if(asnwer == 'нет'):
            break
main()