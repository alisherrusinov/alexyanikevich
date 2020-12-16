import sys
import random

def generate(n,m):
    return [[random.randrange(1,51) for i in range(n)] for j in range(m)]

def work():
    n = random.randrange(5,11)
    m = random.randrange(5,11)
    first = generate(n,m)
    second = generate(n,m)
    print('Первая матрица')
    for i in first:
        print(*i)
    print("-------------")
    print('Вторая матрица')
    for i in second:
        print(*i)
    slojenie = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            slojenie[i][j] = first[i][j]+second[i][j]
    print("-------------")
    print('Сложенная матрица')
    for i in slojenie:
        print(*i)

def is_right(a):
    try:
        a = int(a)
    except ValueError:
        return False
    return a
 
def main():
    while True:
        work()
        asnwer = input("Продолжить? (да/нет) ")
        if(asnwer == 'нет'):
            break
main()