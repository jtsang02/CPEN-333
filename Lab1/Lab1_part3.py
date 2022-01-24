# student name:     Josiah Tsang
# student number:   74191248

import turtle

turtle.pensize(7)
colors = ['black', 'blue','red', 'yellow', 'green']             # list of different colors
coordinates = [(0,0), (-100,0), (100,0), (-50,-50), (50, -50)]  #coordinates of each ring

for i in range(5):  
    turtle.goto(coordinates[i])                                 # set coordinate
    turtle.pendown()                                            # pen down to draw circle
    turtle.color(colors[i])                                     # set color
    turtle.circle(45)                                           # draw circle of size r=45
    turtle.penup()                                              # pen up to move coordinates

turtle.hideturtle()
turtle.done()
