# from turtle import Turtle,Screen
# import random
# turd=Turtle()
# print(turd)
# turd.shape('turtle')
# p=['blue','red','purple','pink','yellow','black']
# turd.speed(10)
# for i in range(36):
#     turd.color(random.choice(p))
#     turd.circle(100)
#     turd.left(10)
    
# scr=Screen()
# print(scr.canvheight)
# scr.exitonclick()



# import colorgram
# colors=colorgram.extract("D:\downloads\image.jpg",25)
# l=[]
# for i in colors:
#     n=(i.rgb.r,i.rgb.g,i.rgb.b)
#     l.append(n)
# print(l)

import turtle as t
import random
turd=t.Turtle()
t.colormode(255)
turd.speed(300)
c=[(199, 163, 119), (216, 209, 212), (210, 213, 218), (165, 187, 163), (38, 95, 116), (125, 38, 29), (51, 35, 34), (156, 77, 55), (114, 73, 82), (119, 163, 174), (196, 99, 73), (49, 130, 103), (126, 34, 42), (18, 56, 42), (215, 197, 121), (7, 65, 84), (102, 149, 73), (186, 152, 156), (78, 35, 38), (216, 158, 29), (176, 202, 180), (19, 80, 97), (218, 180, 171)]
for i in range(10):
    for j in range(10):
        turd.pendown()
        turd.dot(20,random.choice(c))
        turd.penup()
        if j!=9:
            turd.forward(50)
    if i%2==0:
        turd.left(90)
        turd.forward(50)
        turd.left(90)
    else:
        turd.right(90)
        turd.forward(50)
        turd.right(90)
scr=t.Screen()
scr.exitonclick()            
    
        
        
