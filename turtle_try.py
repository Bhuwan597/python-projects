import turtle

# create a turtle object
my_turtle = turtle.Turtle()

# set the turtle's speed and color
my_turtle.speed(1)
my_turtle.pensize(2)
my_turtle.color('red')

# draw a heart shape
my_turtle.begin_fill()
my_turtle.left(45)
my_turtle.forward(100)
my_turtle.circle(50, 180)
my_turtle.right(90)
my_turtle.circle(50, 180)
my_turtle.forward(100)
my_turtle.end_fill()
my_turtle.forward(100)


# hide the turtle
my_turtle.hideturtle()

# keep the turtle window open until you close it
turtle.done()
