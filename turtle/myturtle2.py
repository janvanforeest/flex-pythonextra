import turtle
turtle.speed(0)
colors = ["Red","Blue","Brown","LimeGreen"]
colors2 = ["Cyan","Magenta","Yellow","DarkBlue"]
#my_fill = turtle.fill(colors)
turtle.begin_fill()
my_pen = turtle.Pen()
turtle.bgcolor("DimGray")
for x in range(200):
    turtle.fillcolor(colors[x % 4])
    my_pen.pencolor(colors2[x % 4])
    my_pen.width(20)
    my_pen.forward(20)
    my_pen.left(46)
    my_pen.forward(20)
    my_pen.left(46)
    my_pen.forward(20)
    my_pen.left(46)
    my_pen.forward(20)
    my_pen.left(46)
    my_pen.forward(20)
    my_pen.left(46)
    my_pen.forward(20)
    my_pen.left(46)
    my_pen.forward(20)
    my_pen.left(46)
    my_pen.forward(20)
    my_pen.right(2)
    turtle.fill()

turtle.done()