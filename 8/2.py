from random import randrange
def work():
    answer = {}
    answer[1] = randrange(1,7)
    answer[2] = [randrange(1,7),randrange(1,7)]
    answer[3] = [randrange(1,7),randrange(1,7),randrange(1,7)]
    answer[4] = [randrange(1,7),randrange(1,7),randrange(1,7),randrange(1,7)]
    return answer

def is_right(a):
    try:
        a = int(a)
        if(a not in [1,2,3,4]):
            return False
    except ValueError:
        return False
    return a
 
def main():
    while True:
        a = input('Выберите вариант (1-4): ')
        a = is_right(a)
        if(a is False):  
            print('Введите корректное число ')
            continue
        kub = work()
        try:
            print(*kub[a])
        except TypeError:
            print(kub[a])
        asnwer = input("Продолжить? (да/нет) ")
        if(asnwer == 'нет'):
            break
main()