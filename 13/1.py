from math import sqrt
def work(x1,y1,x2,y2):
    s = sqrt((x2-x1)**2 + (y2-y1)**2)
    return s

def is_right(a):
    try:
        a = float(a)
    except ValueError:
        return False
    return a
 
def main():
    while True:
        x1 = input('Введите x1 ')
        x1 = is_right(x1)
        if(x1 is False):
            print('Введите корректное число')
            continue

        x2 = input('Введите x2 ')
        x2 = is_right(x2)
        if(x2 is False):
            print('Введите корректное число')
            continue

        у1 = input('Введите у1 ')
        у1 = is_right(у1)
        if(у1 is False):
            print('Введите корректное число')
            continue

        у2 = input('Введите у2 ')
        у2 = is_right(у2)
        if(у2 is False):
            print('Введите корректное число')
            continue
        s = work(x1,у1,x2,у2)
        print(s)
        asnwer = input("Продолжить? (да/нет) ")
        if(asnwer == 'нет'):
            break
main()