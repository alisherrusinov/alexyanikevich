def china_calendar(n):
    if n % 12 == 0:
        res = 'год обезъяны'
        print(res)
    elif n % 12 == 1:
        res = 'год петуха'
        print(res)
    elif n % 12 == 2:
        res = 'год србаки '
        print(res)
    elif n % 12 == 3:
        res = 'год свиньи  '
        print(res)
    elif n % 12 == 4:
        res = 'год мыши   '
        print(res)
    elif n % 12 == 5:
        res = 'год быка   '
        print(res)
    elif n % 12 == 6:
        res = 'год тигра   '
        print(res)
    elif n % 12 == 7:
        res = 'год кролика   '
        print(res)
    elif n % 12 == 8:
        res = 'год дракона   '
        print(res)
    elif n % 12 == 9:
        res = 'год змеи   '
        print(res)
    elif n % 12 == 10:
        res = 'год лошади   '
        print(res)
    elif n % 12 == 11:
        res = 'год овцы   '
        print(res)
 

def is_right(a):
    try:
        a = int(a)
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
        china_calendar(a)
        asnwer = input("Продолжить? (да/нет) ")
        if(asnwer == 'нет'):
            break
main()