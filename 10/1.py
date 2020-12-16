 
def work(a):
    if(a<-20):
        print('Холодновато')
    elif(a in range(-19,1)):
        print('Не жарко')
    elif(a in range(0,21)):
        print('Сравнительно нормально')
    elif(a in range(25,31)):
        print('Жарковато')
    elif(a>30):
        print('На улице очень жарко')


def is_right(a):
    try:
        a = int(a)
        print(a)
    except ValueError:
        return False
    return a
 
def main():
    while True:
        a = input('Введите 1 число ')
        a = is_right(a)
        if(a is False):  
            print('Введите корректное число ')
            continue
        work(a)
        asnwer = input("Продолжить? (да/нет) ")
        if(asnwer == 'нет'):
            break
main()