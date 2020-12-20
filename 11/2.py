

def work(a,name,surname):
    print(f'{name} {surname} вам {2020-a} лет')


def is_right(a):
    try:
        a = int(a)
        if(a>2020):
            return False
    except ValueError:
        return False
    return a
 
def main():
    while True:
        surname = input('Введите фамилию ')
        name = input('Введите имя ')
        a = input('Введите год рождения')
        a = is_right(a)
        if(a is False):  
            print('Введите корректное число ')
            continue
        work(a,name,surname)
        asnwer = input("Продолжить? (да/нет) ")
        if(asnwer == 'нет'):
            break
        
main()