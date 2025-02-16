#Library or Module is to draw

import turtle

#screen() is similer to draw window
#Turtle() is pen 
paper = turtle.Screen()
pen = turtle.Turtle()

while True:
    draw =input('What we can Draw:')
    print(draw)
   

    #condition statements
    if draw == 'pentagon':
        side = 5
    if draw == 'hexagon':
        side = 6
    if draw == 'octagon':
        side = 8
    if draw == 'triangle':
        side = 3
    if draw == 'square':
        side = 4
    if draw == 'heptagon':
        side = 7
    if draw == 'nonagon':
        side = 9
    if draw == 'decagon':
        side = 10
    if draw == 'lcosagon':
        side = 20

    for time in range(side):
        #indentation tab
        pen.fd(100)
        pen.right(360/side)

