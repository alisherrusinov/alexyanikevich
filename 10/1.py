
import cmath, random


def work(a):
    randoms = [[random.random(),random.random()] for x in range(a)]
    print(randoms)

    print(cmath.pi/4)
    print(3.14/4)

    if(cmath.pi/4>3.14/4):
        print('Pi/4 больше на ', cmath.pi/4-3.14/4)


def is_right(a):
    try:
        a = int(a)
    except ValueError:
        return False
    return a
 
def main():
    while True:
        a = input('Введите 1 число ')
        a = is_right(a)
        if(a<0):
            break
        work(a)
        if(a is False):  
            print('Введите корректное число ')
            continue
        
main()