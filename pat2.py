from turtle import *
speed('fastest')
bgcolor('black')
colors = ['black','brown','black',
          'black','brown','black']
i = 0
while True:
    pencolor (colors[i%6])
    pensize(3)
    fd(10 + i)
    lt(58)
    i += 1  
mainloop()