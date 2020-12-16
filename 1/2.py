def work(n):
    answer = []
    while n>1:
        if(n%2 == 0):
            n = n/2
            answer.append(int(n))
        else:
            n = 3*n+1
            answer.append(int(n))
        work(n)
    return answer

def is_right(a):
    try:
        a = int(a)
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
        wor = work(a)
        print(*wor)
        asnwer = input("Продолжить? (да/нет) ")
        if(asnwer == 'нет'):
            break
main()