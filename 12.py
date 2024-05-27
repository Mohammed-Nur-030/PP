import turtle

def sierpinski(t, x, y, size, depth, change_depth=None):
    if depth == 0:
        t.penup()
        t.goto(x, y)
        t.pendown()
        for _ in range(3):
            t.forward(size)
            t.left(120)
    else:
        sierpinski(t, x, y, size / 2, depth - 1)
        sierpinski(t, x + size / 2, y, size / 2, depth - 1)
        sierpinski(t, x + size / 4, y + (size / 2) * (3 ** 0.5) / 2, size / 2, depth - 1)

        if change_depth is not None and depth == change_depth:
            t.fillcolor('magenta')
            t.begin_fill()
            sierpinski(t, x + size / 4, y + (size / 2) * (3 ** 0.5) / 2, size / 2, 0)
            t.end_fill()
            
            t.fillcolor('red')
            t.begin_fill()
            sierpinski(t, x, y, size / 2, 0)
            t.end_fill()
            
            t.fillcolor('blue')
            t.begin_fill()
            sierpinski(t, x + size / 2, y, size / 2, 0)
            t.end_fill()

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed

    depth = 4  # Depth of recursion
    change_depth = 2  # Depth at which to change the colors

    size = 400  # Size of the triangle
    x = -200  # Initial x position
    y = -200  # Initial y position

    sierpinski(t, x, y, size, depth, change_depth)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
