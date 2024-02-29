# William Beckham
# P4LAB1
# Write a turtle graphics programs that draws a triangle and a square using loops.


import turtle


# Function to draw a triangle
def draw_triangle(t):
    for _ in range(3):
        t.forward(100) 
        t.left(120)

# Function to draw a square
def draw_square(t):
    for _ in range(4):
        t.right(90)
        t.forward(100)

def main():
    # Create screen and turtle objects
    s = turtle.Screen()
    t = turtle.Turtle()

    # Set screen size and background color
    s.setup(800, 800)  
    s.bgcolor("black")

    # Set turtle properties
    t.pensize(5)  # Set line thickness
    t.pencolor("pink")
    t.fillcolor("pink")
    t.begin_fill()


    # Draw the first triangle
    draw_triangle(t)

    t.forward(100)

    # Draw the second triangle
    draw_triangle(t)

    t.forward(50)

    # Draw a square box centered under the triangles
    draw_square(t)

    t.end_fill()
    t.penup()

    # Draw a simple face on kitty 
    t.pencolor("black")
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(20)
    t.pendown()
    t.forward(3)
    t.penup()
    t.forward(42)
    t.pendown()
    t.forward(3)
    t.penup()
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.pendown()
    t.forward(3)
    t.penup()
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(15)
    t.pendown()
    t.back(24)
    t.penup()

    print("meow I'm a kitty meow")

    # Keep the window open
    turtle.done()

if __name__ == '__main__':
    main()