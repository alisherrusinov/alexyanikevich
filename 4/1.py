def es_perfecto(n):
    suma = 1
    i = 2
    while i * i < n + 1 :
        if n % i == 0 :
            suma+=i
            if i != n // i :
                suma += n // i
        i += 1
    return suma == n
 
 
def work(n):
    listt = []
    for i in range(2,n+1):
        if es_perfecto(i):
            listt.append(i)
    print(listt)


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