 
def work(string):
    reversed_string = string[::-1]
    return string == reversed_string

def is_right(a):
    try:
        a = str(a)
    except ValueError:
        return False
    return a
 
def main():
    while True:
        a = input('Введите строку ')
        a = is_right(a)
        if(not a):  
            print('Введите корректное число ')
            continue
        if(work(a)):
            print('Строка является палиндромом')
        else:
            print('Строка не является палиндромом')
        asnwer = input("Продолжить? (да/нет) ")
        if(asnwer == 'нет'):
            break
main()