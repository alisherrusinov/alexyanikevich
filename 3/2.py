from math import pi

def work(r):
    print("Объём шара: ",4/3*pi*r**3)
    print("Площать поверхности шара: ",4*pi*r**2)

def is_right(a):
    try:
        a = float(a)
    except ValueError:
        return False
    return a
 
def main():
    while True:
        a = input('Введите число ')
        a = is_right(a)
        if(not a):
            print('Введите корректное число ')
            continue
        work(a)
        asnwer = input("Продолжить? (да/нет) ")
        if(asnwer == 'нет'):
            break
main()