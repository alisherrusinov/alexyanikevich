import turtle


def draw(t):
    for i in [10,20,30]:
        t.circle(i)


def work(x, y):
    t = turtle.Turtle()
    t.speed(5)
    t.up()
    t.goto(x, y)
    t.right(90)
    t.down()
    draw(t)
    

    
    
 
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
        b = input('Введите число ')
        b = is_right(b)
        if(not b):
            print('Введите корректное число ')
            continue
        work(a,b)
        asnwer = input("Продолжить? (да/нет) ")
        if(asnwer == 'нет'):
            break
main()