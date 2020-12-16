def work(n):
    # а-я, о-е, у-ю, ы-и, э-е
    glasnie = ['а','я','о','е','у','ю','ы','и','э','e']
    # б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ
    solgasnie = ["б","в","г","д","ж","з","й","к","л","м","н","п","р","р","с","т","ф","х","ц","ч","ш","щ"]
    count = 0
    count1 = 0
    for i in n:
        if(i in glasnie):
            count+=1
        else:
            count1+=1
    print('Гласных: ',count)
    print("Согласных:", count1)

def is_right(a):
    # а-я, о-е, у-ю, ы-и, э-е
    glasnie = ['а','я','о','е','у','ю','ы','и','э','e']
    # б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ
    solgasnie = ["б","в","г","д","ж","з","й","к","л","м","н","п","р","р","с","т","ф","х","ц","ч","ш","щ"]
    for i in a:
        if(i not in glasnie and i not in solgasnie):
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