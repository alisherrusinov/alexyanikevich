 
def work(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    print('Дискриминант = ' + str(discriminant))
    if discriminant < 0:
        print('Корней нет')
    elif discriminant == 0:
        x = -b / (2 * a)
        print('x = ' + str(x))
    else:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        print('x₁ = ' + str(x1))
        print('x₂ = ' + str(x2))

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
        if(a is False):  
            print('Введите корректное число ')
            continue

        b = input('Введите 2 число ')
        b = is_right(b)
        if(b is False):
            print('Введите корректное число ')
            continue

        c = input('Введите 3 число ')
        c = is_right(c)
        if(c is False):  
            print('Введите корректное число ')
            continue
        work(a,b,c)
        asnwer = input("Продолжить? (да/нет) ")
        if(asnwer == 'нет'):
            break
main()