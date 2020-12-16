

def is_right(a):
    try:
        a = int(a)
        print(a)
    except ValueError:
        return False
    return a

import random 
def work():
    correct = random.randrange(0,101)
    answer = 0
    tries = 0
    while True:
        answer = int(input('Введите ваш вариант: '))
        answer = is_right(answer)
        if(answer == correct):
            print('Правильно!')
            print('Попыток: ', tries)
            break
        else:
            print("Неправильно")
            if(answer>correct):
                print('Загаданное число меньше')
            else:
                print('Загаданное число больше')
            tries+=1 


def main():
    while True:
        work()
        asnwer = input("Продолжить? (да/нет) ")
        if(asnwer == 'нет'):
            break
main()