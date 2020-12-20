
def work(a):
    #а-я, о-е, у-ю, ы-и, э-е
    glasnie = ['а','я','о','e','у','ю','ы','и','э','e']
    answer = ''
    
    for i in a:
        if(i not in glasnie):
            answer+=i
    print(answer)

def is_right(a):
    try:
        a = str(a)
    except ValueError:
        return False
    return a
 
def main():
    while True:
        a = input('Введите слово ')
        a = is_right(a)
        if(a is False):  
            print('Введите корректное слово ')
            continue
        work(a)
        asnwer = input("Продолжить? (да/нет) ")
        if(asnwer == 'нет'):
            break
        
main()