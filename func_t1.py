from turtle import*

def hexagon(size):
    for i in range(6):
        forward(size)
        lt(72)



def square(size, color='brown'):
    fillcolor(color)
    begin_fill()
    for i in range(4):
        forward(size)
        rt(90)
    end_fill()

hexagon(100)
hexagon(50)
square(100,'blue')
square(50,'green')




