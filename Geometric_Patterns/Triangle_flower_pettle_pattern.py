import turtle                # Import the turtle graphics module for drawing
import colorsys              # Import colorsys module to handle HSV to RGB color conversion

# Setup screen
screen = turtle.Screen()    # Create a screen/window for the turtle graphics
screen.bgcolor("black")     # Set the background color of the screen to black
screen.title("Triangle Rangoli with Center Flower")  # Set the title of the window
turtle.colormode(1.0)      # Set color mode to use float RGB values between 0 and 1

# Create turtle
pen = turtle.Turtle()       # Create a turtle object named pen for drawing
pen.speed(0)                # Set drawing speed to the fastest
pen.width(2)                # Set pen width to 2 pixels
pen.hideturtle()            # Hide the turtle cursor (arrow) for cleaner drawing

# Generate rainbow colors
def generate_colors(n):     # Define a function to generate n colors evenly spaced in HSV hue
    return [colorsys.hsv_to_rgb(i/n, 1.0, 1.0) for i in range(n)]  # Return list of RGB colors converted from HSV

colors = generate_colors(100)  # Generate 100 colors from hue 0 to 1 for smooth rainbow effect

# Draw equilateral triangle
def draw_triangle(size):    # Define function to draw a triangle of given side length
    for _ in range(3):      # Repeat 3 times (3 sides)
        pen.forward(size)   # Move pen forward by 'size' units (draw one side)
        pen.left(120)       # Turn left by 120 degrees to get an equilateral triangle

# Draw a ring of triangles
def draw_triangle_ring(radius, count, size, rotation_offset=0):  # Draw 'count' triangles in a circle of radius 'radius'
    for i in range(count):   # Loop through each triangle to draw in the ring
        angle = 360 / count  # Calculate angle between each triangle placement
        pen.penup()          # Lift pen to move without drawing
        pen.goto(0, 0)       # Move turtle to center (origin)
        pen.setheading(angle * i + rotation_offset)  # Point turtle at the correct angle with optional rotation offset
        pen.forward(radius)  # Move turtle forward to the ring radius
        pen.pendown()        # Put pen down to start drawing
        pen.setheading(angle * i + rotation_offset)  # Ensure heading is correct before drawing triangle
        pen.color(colors[(i * 7) % len(colors)])  # Set color from colors list with step of 7 for color variation
        pen.begin_fill()     # Start filling the shape
        draw_triangle(size)  # Draw a triangle of given size at this position
        pen.end_fill()       # Fill the triangle with chosen color

# Draw petal using arcs
def draw_petal(radius, angle):  # Draw a petal shape using two arcs
    for _ in range(2):           # Repeat twice to form a symmetrical petal
        pen.circle(radius, angle)  # Draw arc of circle with given radius and angle
        pen.left(180 - angle)      # Turn left to position for the second arc (mirror arc)

# Draw a flower with arc petals
def draw_flower(petals, radius, angle, size):  # Draw a flower with given number of petals and arc parameters
    for i in range(petals):          # Loop through each petal to draw
        pen.color(colors[i % len(colors)])  # Set color for the petal cycling through colors list
        pen.begin_fill()              # Start filling the petal shape
        draw_petal(size, angle)       # Draw one petal using arcs
        pen.end_fill()                # Fill the petal with color
        pen.left(360 / petals)        # Rotate turtle to position for the next petal

# === Draw central flower ===
pen.penup()                # Lift pen to move without drawing
pen.goto(0, 0)             # Move to center of the screen
pen.setheading(0)          # Set heading to 0 degrees (point right)
pen.pendown()              # Put pen down to start drawing
draw_flower(petals=24, radius=10, angle=60, size=30)  # Draw flower with 24 petals, arc size 30, and 60 degrees arc angle

# Draw central triangle flower
pen.penup()                # Lift pen to move without drawing
pen.goto(0, 0)             # Move back to center
pen.setheading(0)          # Reset heading to 0 degrees
pen.pendown()              # Put pen down to draw
draw_triangle_ring(radius=40, count=6, size=15)  # Draw a ring of 6 triangles at radius 40 and size 15

# === Triangle Rings ===
draw_triangle_ring(radius=80, count=12, size=60)             # Draw ring of 12 large triangles at radius 80
draw_triangle_ring(radius=140, count=18, size=50, rotation_offset=10)  # Draw ring of 18 triangles, rotated by 10 degrees
draw_triangle_ring(radius=200, count=24, size=40, rotation_offset=20)  # Draw ring of 24 triangles, rotated by 20 degrees
draw_triangle_ring(radius=260, count=30, size=20, rotation_offset=15)  # Draw ring of 30 smaller triangles, rotated by 15 degrees

turtle.done()  # Finish turtle drawing and display the window until closed
