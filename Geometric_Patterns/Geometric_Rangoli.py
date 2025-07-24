# Import the turtle graphics module and colorsys for color manipulation
import turtle
import colorsys

# Setup the drawing screen
screen = turtle.Screen()               # Create a screen object
screen.bgcolor("black")                # Set the background color to black
screen.title("Traditional Rangoli Design")  # Set the window title
turtle.colormode(1.0)                  # Set color mode to 1.0 (HSV color values between 0 and 1)

# Create and configure the turtle (pen) used for drawing
pen = turtle.Turtle()                 # Create a turtle object
pen.speed(0)                          # Set the fastest drawing speed
pen.width(2)                          # Set the pen width to 2 pixels
pen.hideturtle()                      # Hide the turtle cursor for clean drawing

# Function to generate 'n' distinct colors using HSV color space
def generate_colors(n):
    return [colorsys.hsv_to_rgb(i/n, 1.0, 1.0) for i in range(n)]  # Return a list of RGB colors converted from HSV

colors = generate_colors(100)         # Generate 100 colors and store them in a list

# Function to draw a regular polygon of given sides and size
def draw_polygon(sides, size):
    angle = 360 / sides               # Calculate angle between each side
    for _ in range(sides):           
        pen.forward(size)             # Draw a side
        pen.right(angle)              # Turn by the angle

# Function to draw a petal shape using arcs (part of a circle)
def draw_petal(radius, angle):
    for _ in range(2):
        pen.circle(radius, angle)     # Draw an arc of a circle
        pen.left(180 - angle)         # Turn to draw the opposite arc for symmetry

# Function to draw a flower with multiple petals
def draw_flower(petals, radius, angle):
    for i in range(petals):
        pen.color(colors[i % len(colors)])  # Set pen color from color palette
        pen.begin_fill()              # Start filling the petal
        draw_petal(radius, angle)     # Draw a petal
        pen.end_fill()                # End filling the petal
        pen.left(360 / petals)        # Rotate to position for next petal

# Function to draw a ring of shapes arranged radially
def draw_shape_ring(shape_func, radius, count, size):
    for i in range(count):
        pen.penup()
        pen.goto(0, 0)                # Return to the center
        pen.setheading(i * (360 / count))  # Set heading direction
        pen.forward(radius)           # Move outward from the center
        pen.pendown()
        pen.setheading(i * (360 / count))  # Align shape orientation
        pen.color(colors[(i * 5) % len(colors)])  # Choose a color
        shape_func(size)              # Draw the shape using the given function

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        pen.forward(size)             # Draw one side
        pen.right(90)                 # Turn 90 degrees

# Function to draw a rectangle (length = size, width = size/2)
def draw_rectangle(size):
    for _ in range(2):
        pen.forward(size)             # Draw longer side
        pen.right(90)
        pen.forward(size / 2)         # Draw shorter side
        pen.right(90)

# Function to draw a triangle
def draw_triangle(size):
    for _ in range(3):
        pen.forward(size)             # Draw one side
        pen.right(120)                # Turn 120 degrees to make an equilateral triangle

# Draw a central filled white circle
pen.penup()
pen.goto(0, -30)                      # Move turtle to draw circle centered at (0,0)
pen.pendown()
pen.color("white")                    # Set fill color
pen.begin_fill()
pen.circle(30)                        # Draw circle with radius 30
pen.end_fill()

# Draw flower at the center
pen.penup()
pen.goto(0, 0)                        # Move to center
pen.setheading(0)                     # Face right
pen.pendown()
draw_flower(petals=12, radius=60, angle=60)  # Draw flower with 12 petals

# Draw a ring of 12 triangles at radius 100
draw_shape_ring(draw_triangle, radius=100, count=12, size=50)

# Draw a ring of 12 squares at radius 150
draw_shape_ring(draw_square, radius=150, count=12, size=50)

# Draw a ring of 12 rectangles at radius 200
draw_shape_ring(draw_rectangle, radius=200, count=12, size=70)

# Draw 24 small colored circles around the outermost ring
for i in range(24):
    angle = i * (360 / 24)            # Calculate angle for each circle
    pen.penup()
    pen.goto(0, 0)                    # Return to center
    pen.setheading(angle)            # Set heading to current angle
    pen.forward(250)                 # Move outward to desired radius
    pen.pendown()
    pen.color(colors[i % len(colors)])  # Set a color from palette
    pen.begin_fill()
    pen.circle(10)                   # Draw a small circle of radius 10
    pen.end_fill()

turtle.done()                         # Finish the drawing and keep the window open
