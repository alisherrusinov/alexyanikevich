

def work(a):
    if(a>3):
        print('Превышен лимит')
        return False
    print('Цена заказа:', 1230*a+100+(50*a))


def is_right(a):
    try:
        a = float(a)
    except ValueError:
        return False
    return a
 
def main():
    while True:
        a = input('Введите количество ')
        a = is_right(a)
        if(a is False):  
            print('Введите корректное число ')
            continue
        work(a)
        asnwer = input("Продолжить? (да/нет) ")
        if(asnwer == 'нет'):
            break
        
main()