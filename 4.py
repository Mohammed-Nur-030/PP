import turtle

# Ask user for number of sides, length of side, color, and fill color
num_sides = int(input("Enter the number of sides: "))
side_length = int(input("Enter the length of each side: "))
pen_color = input("Enter the pen color: ")
fill_color = input("Enter the fill color: ")

# Set up turtle
t = turtle.Turtle()
t.color(pen_color)
t.fillcolor(fill_color)

# Draw polygon
angle = 360 / num_sides
t.begin_fill()
for i in range(num_sides):
    t.forward(side_length)
    t.right(angle)
t.end_fill()

# Keep turtle window open until user clicks to close
turtle.done()
