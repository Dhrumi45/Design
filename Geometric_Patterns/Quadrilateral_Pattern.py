import turtle               # Import the turtle graphics module for drawing
import colorsys             # Import colorsys for color conversions (HSV to RGB)

# Setup screen
screen = turtle.Screen()    # Create a screen/window for turtle graphics
screen.bgcolor("black")     # Set background color of the screen to black
screen.title("Square-Only Rangoli")  # Set the window title
turtle.colormode(1.0)       # Set color mode to use float values between 0 and 1 for RGB

# Create turtle
pen = turtle.Turtle()       # Create a turtle object named pen to draw
pen.speed(0)                # Set the drawing speed to the fastest (0 means no animation delay)
pen.width(2)                # Set the pen width (thickness) to 2 pixels
pen.hideturtle()            # Hide the turtle cursor (the arrow icon) from the screen

# Generate colors
def generate_colors(n):
    # Create a list of n colors evenly spaced in HSV hue spectrum, converted to RGB
    return [colorsys.hsv_to_rgb(i/n, 1.0, 1.0) for i in range(n)]

colors = generate_colors(100)  # Generate a palette of 100 colors

# Draw a square
def draw_square(size):
    # Draw a square with side length 'size'
    for _ in range(4):          # Repeat 4 times (for 4 sides)
        pen.forward(size)       # Move pen forward by 'size' pixels
        pen.right(90)           # Turn pen right by 90 degrees to form right angles

# Draw a ring of squares arranged in a circle
def draw_square_ring(radius, count, size, rotation_offset=0):
    # radius: distance from center to the position of each square
    # count: how many squares to draw in the ring
    # size: side length of each square
    # rotation_offset: angle offset to rotate the entire ring of squares
    for i in range(count):       # Loop through each square in the ring
        angle = 360 / count      # Angle between each square in degrees
        pen.penup()              # Lift pen to move without drawing
        pen.goto(0, 0)           # Go to center of screen
        pen.setheading(angle * i + rotation_offset)  # Face the direction for this square in the ring
        pen.forward(radius)      # Move forward to the ring radius
        pen.pendown()            # Put pen down to start drawing
        pen.setheading(angle * i + rotation_offset + 45)  # Tilt square by 45 degrees for petal effect
        pen.color(colors[(i * 5) % len(colors)])  # Set pen color cycling through generated colors
        pen.begin_fill()         # Start filling the shape
        draw_square(size)        # Draw a square of the specified size
        pen.end_fill()           # Fill the drawn square with current color

# Draw center square at fixed position
pen.penup()                    # Lift pen to move without drawing
pen.goto(-20, 20)              # Move to coordinates (-20, 20)
pen.pendown()                  # Put pen down to start drawing
pen.color("white")             # Set pen color to white
pen.begin_fill()               # Start filling shape
draw_square(40)                # Draw a square of size 40 pixels
pen.end_fill()                 # Fill the square with white color

# Draw multiple layers of square rings with increasing radius and counts
draw_square_ring(radius=70, count=8, size=40)               # First ring: 8 squares at radius 70
draw_square_ring(radius=120, count=16, size=30, rotation_offset=15)  # Second ring: 16 squares at radius 120, rotated 15 degrees
draw_square_ring(radius=170, count=32, size=20, rotation_offset=30)  # Third ring: 32 squares at radius 170, rotated 30 degrees
draw_square_ring(radius=220, count=64, size=15, rotation_offset=45)  # Fourth ring: 64 squares at radius 220, rotated 45 degrees

turtle.done()                 # Finish drawing and keep the window open until closed by user