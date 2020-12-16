import sys
import random

def generate(n):
    return [[random.randrange(sys.maxsize) for i in range(n)] for j in range(n)]

def work():
    n = random.randrange(5,11)
    first = generate(n)
    second = generate(n)
    print('Первая матрица')
    for i in first:
        print(*i)
    print("-------------")
    print('Вторая матрица')
    for i in second:
        print(*i)
    slojenie = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            slojenie[i][j] = first[i][j]+second[i][j]
    print("-------------")
    print('Сложенная матрица')
    for i in slojenie:
        print(*i)
    umnojenie = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            umnojenie[i][j] = first[i][j]*second[i][j]
    print("-------------")
    print('Перемноженная матрица')
    for i in umnojenie:
        print(*i)

def is_right(a):
    try:
        a = int(a)
    except ValueError:
        return False
    return a
 
def main():
    while True:
        wor = work()
        print(wor)
        asnwer = input("Продолжить? (да/нет) ")
        if(asnwer == 'нет'):
            break
main()