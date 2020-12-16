def work(n):
    if(n>8):
        print('Почти все строения рухнули')
    elif(n>7):
        print('Многие здания разрушены')
    elif(n>6):
        print('Многие здания значительно повреждены, некоторые разрушены.')
    elif(n>4.5):
        print("Повреждены здания, имеющие дефекты.")
    else:
        print("Повреждений практически нет")

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