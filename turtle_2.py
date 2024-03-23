from turtle import Turtle, Screen

def drawing_polygon(turtle, sides, color, direction):
    turtle.pencolor(color)
    for _ in range(sides):
        turtle.fd(100)
        turtle.right(direction)

values = [{"sides": sides, "color": color, "direction": direction}
    for sides, color, direction in [(3, "red", 120), (4, "purple", 90), (5, "blue", 72), (6, "green", 60), 
                                    (7, "yellow", 51.42), (8, "orange", 45), (9, "pink", 40), (10, "brown", 36)]]

timmy_the_turtle = Turtle(shape="turtle", visible=True)
timmy_the_turtle.speed(1)
timmy_the_turtle.pensize(3)

for i in values:
    drawing_polygon(timmy_the_turtle, **i)

Screen().exitonclick()