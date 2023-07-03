from turtle import *
speed('fastest')
colors = ['red' , 'purple']
bgcolor('black')
pensize(2)
for i in range(6):
    pencolor('red')
    fd(100)
    for i in range(3):
        pencolor('green')
        fd(50)
        fillcolor(colors[i%2])
        begin_fill()
        for i in range (3):
            pencolor('blue')
            fd(25)
            lt(360/3)
        end_fill()
        lt(360/3)
    lt(360/6)
mainloop()