from turtle import *
# # hideturtle()

# rectangle draw
color('green')
begin_fill()
fillcolor('green')
forward(180)
left(90)
forward(100)
left(90)
forward(180)
left(90)
forward(100)
end_fill()
# circle draw
color('red')
fillcolor('red')
begin_fill()
penup()
goto(70,50)
pendown()
circle(20)
end_fill()
# stick draw
color('black')
penup()
goto(0,100)
pensize(10)
pendown()
forward(300)