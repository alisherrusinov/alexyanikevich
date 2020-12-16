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
    

    for i in range(1,4):
        t.up()
        t.right(90)
        t.goto(x,y-60*i)
        t.left(90)
        t.down()
        draw(t)
    t.up()
    t.goto(x+60,y-180)
    t.down()
    draw(t)
    
    t.up()
    for i in range(2,4):
        t.goto(x+60*i,y-180)
        t.down()
        draw(t)
        t.up()
    

    t.goto(x+60,y-120)
    t.down()
    draw(t)
    
    t.up()
    t.goto(x+120,y-60)
    t.down()
    draw(t)
    
    t.up()
    t.goto(x+180,y)
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