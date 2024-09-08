# from turtle import Screen,Turtle
# turd2=Turtle()
# scr=Screen()
# turd2.speed('fastest')

# def fwd():
#     turd2.forward(5)

# def bwd():
#     turd2.back(5)

# def clockwise():
#     n=turd2.heading() - 20
#     turd2.setheading(n)

# def anticlockwise():
#     n=turd2.heading() + 20
#     turd2.setheading(n)

# def clean():
#     turd2.clear()
#     turd2.reset()



# scr.listen()
# scr.onkey(fwd,'w')
# scr.onkey(bwd,'s')
# scr.onkey(anticlockwise,'a')
# scr.onkey(clockwise,'d')
# scr.onkey(clean,'c')

# scr.exitonclick()

from turtle import Screen,Turtle
import random
scr=Screen()
scr.setup(width=500,height=400)
inp=scr.textinput(title='Make your bet', prompt="Which color will win?")
t1=Turtle(shape='turtle')
t2=Turtle(shape='turtle')
t3=Turtle(shape='turtle')
t4=Turtle(shape='turtle')
t1.color('red')
t2.color('green')
t3.color('orange')
t4.color('purple')
t=[t1,t2,t3,t4]
for i in t:
    i.penup()
t1.goto(x=-230,y=150)
t2.goto(x=-230,y=50)
t3.goto(x=-230,y=-50)
t4.goto(x=-230,y=-150)

end=False
while end!=True:
    random.choice(t).forward(10)
    for i in t:
        if i.xcor()>220:  
            if i.pencolor()==inp:
                print("you win")
            else:
                print("you lose")
            end=True
            break
    
scr.exitonclick()