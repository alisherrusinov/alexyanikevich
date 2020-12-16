
def is_eazy(n):
    count = 0
    for i in range(1,n+1):
        if(n%i == 0):
            count+=1
    if(count == 2):
        return n
    else:
        return False
 
 
def work(n):
    answer = []
    for i in range(1,n+1):
        a = is_eazy(i)
        if a is not False:
            answer.append(a)
    print(*answer)

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
        work(a)
        asnwer = input("Продолжить? (да/нет) ")
        if(asnwer == 'нет'):
            break
main()