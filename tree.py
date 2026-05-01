import turtle
import random

def draw_tree(t,branch_length,angle,shrink):
    if branch_length < 5:
        leaf_color=random.choice(['#FF4500','#FF8C00','#FFD700',"#F6BC3E","#ED932C","#E46C0A"])
        t.color(leaf_color)
        t.begin_fill()
        t.circle(random.randint(1,2))
        t.end_fill()
        t.color("#8F4D1A")
        return
    t.pensize(max(1,branch_length/10))
    # if branch_length >60:
    #     t.color('#3B1F0A')
    # elif branch_length >30:
    #     t.color('#6B3A2A')
    # else:
    #     t.color('#8B5E3C')

    t.color("#7A351E")
    
    t.forward(branch_length)
    t.left(angle)
    draw_tree(t,branch_length*shrink,angle,shrink)
    t.right(angle*2)
    draw_tree(t,branch_length*shrink,angle,shrink)
    t.left(angle)
    t.backward(branch_length)

screen=turtle.Screen()
screen.tracer(1,0)
screen.bgcolor('black')
screen.title('tree')
t=turtle.Turtle()
t.speed(0)
t.hideturtle()
t.left(90)
t.up()
t.goto(0,-200)
t.down()

draw_tree(t,branch_length=100,angle=30,shrink=0.75)
turtle.done()