# William Beckham
# P4LAB1
# 02-29-2024
# Write a turtle graphics programs that draws a triangle and a square using loops.


import turtle

# Function to draw a triangle
def draw_triangle(t):
    for _ in range(3):
        t.forward(150) 
        t.left(120)

# Function to draw a square
def draw_square(t):
    for _ in range(4):
        t.right(90)
        t.forward(400)

# Function to draw small triangles
def draw_sm_triangle(t):
    t.pendown()
    t.pencolor("black")
    t.fillcolor("black")
    t.begin_fill()
    for _ in range(3):
        t.forward(100)
        t.left(120)
    t.end_fill()
    t.penup()

# Function to draw eyes
def draw_eye(t):
    t.pendown()
    t.pencolor("black")
    t.fillcolor("white")
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    t.fillcolor("purple")
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.penup()

# Function to draw nose
def draw_nose(t):
    t.pendown()
    t.pencolor("black")
    t.fillcolor("black")
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    t.penup()

# Function to draw left whiskers  
def draw_left_whisk(t):
    t.goto(-35,-35)
    t.pendown()
    t.back(76)
    t.penup()
    t.goto(-35,-33)
    t.pendown()
    t.left(145)
    t.forward(84)
    t.penup()
    t.goto(-35,-38)
    t.pendown()
    t.right(130)
    t.back(68)
    t.penup()

# Function to draw right whiskers
def draw_right_whisk(t):
    t.goto(35,-35)
    t.pendown()
    t.forward(76)
    t.penup()
    t.goto(35,-33)
    t.pendown()
    t.left(30)
    t.forward(84)
    t.penup()
    t.goto(35,-38)
    t.pendown()
    t.right(65)
    t.forward(68)
    t.penup()

# Function to draw mouth
def draw_mouth(t):
    t.goto(-65,-100)
    t.fillcolor("white")
    t.begin_fill()
    t.pendown()
    t.forward(25)
    t.right(120)
    t.forward(25)
    t.right(120)
    t.forward(25)
    t.end_fill()
    t.penup()
    t.goto(-53,-102)
    t.pendown()
    t.right(100)
    t.forward(110)
    t.penup()
    t.goto(49,-110)
    t.left(30)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    t.forward(25)
    t.right(120)
    t.forward(25)
    t.right(120)
    t.forward(25)
    t.end_fill()
    t.penup()


def main():
    # Create screen and turtle objects
    s = turtle.Screen()
    t = turtle.Turtle()

    # Set screen size and background color
    s.setup(800, 800)  
    s.bgcolor("black")

    # Set turtle properties
    t.pensize(5)  # Set line thickness
    t.speed(2)
    t.penup()
    t.goto(-150,150)
    t.pendown()
    t.pencolor("pink")
    t.fillcolor("pink")
    t.begin_fill()


    # Draw the first triangle
    draw_triangle(t)

    t.forward(150)

    # Draw the second triangle
    draw_triangle(t)

    t.forward(200)

    # Draw a square box centered under the triangles
    draw_square(t)

    t.end_fill()
    t.penup()

    t.goto(-125,150)
    draw_sm_triangle(t)
    t.goto(25,150)
    draw_sm_triangle(t)

    # Draw a simple face on kitty

    t.goto(-75,50)

    draw_eye(t)

    t.goto(70,50)
    t.pendown()
    draw_eye(t)

    t.goto(0,-50)
    draw_nose(t)
    draw_left_whisk(t)
    draw_right_whisk(t)
    draw_mouth(t)

    t.goto(400,400)
    
    print("meow I'm a kitty meow")

    # Keep the window open
    turtle.done()

if __name__ == '__main__':
    main()