def work(a,h):
    print(a)
    print(h)
    print(0.5*a*h)

def is_right(a):
    try:
        a = float(a)
    except ValueError:
        return False
    return a
 
def main():
    while True:
        a = input('Введите основание ')
        a = is_right(a)
        h = input('Введите высоту')
        h = is_right(h)
        if(not a):
            print('Введите корректное число ')
            continue
        if(not h):
            print('Введите корректное число ')
            continue
        work(a,h)
        asnwer = input("Продолжить? (да/нет) ")
        if(asnwer == 'нет'):
            break
main()