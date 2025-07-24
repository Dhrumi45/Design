import turtle  # Turtle graphics library for drawing
import colorsys  # Colorsys module for working with HSV color space

# Setup screen
screen = turtle.Screen()  # Create a screen object for the turtle to draw on
screen.bgcolor("black")  # Set the background color of the screen to black
screen.title("Square-Only Rangoli")  # Set the window title
turtle.colormode(1.0)  # Set color mode to accept float values between 0 and 1

# Create turtle
pen = turtle.Turtle()  # Create a turtle named pen
pen.speed(0)  # Set turtle speed to maximum (fastest drawing)
pen.width(2)  # Set the width of the drawing pen to 2 pixels
pen.hideturtle()  # Hide the turtle cursor for cleaner drawing

# Generate a list of distinct RGB colors using HSV
def generate_colors(n):
    # Return a list of n colors evenly spaced around the HSV color wheel
    return [colorsys.hsv_to_rgb(i/n, 1.0, 1.0) for i in range(n)]

colors = generate_colors(100)  # Generate 100 unique colors and store them

# Function to draw a single square of given size
def draw_square(size):
    for _ in range(4):  # Loop four times to draw four sides
        pen.forward(size)  # Move forward by the given size
        pen.right(90)  # Turn right by 90 degrees to make a square corner

# Function to draw a ring (circle) of tilted squares
def draw_square_ring(radius, count, size, rotation_offset=0):
    for i in range(count):  # Loop to draw 'count' number of squares in a ring
        angle = 360 / count  # Calculate angle between each square
        pen.penup()  # Lift pen to move without drawing
        pen.goto(0, 0)  # Return to center
        pen.setheading(angle * i + rotation_offset)  # Set direction with rotation offset
        pen.forward(radius)  # Move outwards to the radius
        pen.pendown()  # Lower pen to start drawing
        pen.setheading(angle * i + rotation_offset + 45)  # Tilt square 45° for flower-petal look
        pen.color(colors[(i * 5) % len(colors)])  # Choose a color from the generated list
        pen.begin_fill()  # Start filling the square with color
        draw_square(size)  # Draw the square
        pen.end_fill()  # End filling

# Draw the central square in white
pen.penup()  # Lift pen to move to start position
pen.goto(-20, 20)  # Move to top-left of central square
pen.pendown()  # Lower pen to draw
pen.color("white")  # Set color to white
pen.begin_fill()  # Start filling the central square
draw_square(40)  # Draw the central square of size 40
pen.end_fill()  # End filling

# Draw concentric rings of colorful squares with increasing radius and rotation
draw_square_ring(radius=70, count=8, size=40)  # First ring: 8 squares, size 40
draw_square_ring(radius=131, count=12, size=30, rotation_offset=15)  # Second ring: 12 squares
draw_square_ring(radius=181, count=16, size=20, rotation_offset=30)  # Third ring: 16 squares
draw_square_ring(radius=231, count=20, size=15, rotation_offset=45)  # Fourth ring: 20 squares

turtle.done()  # Keep the window open until closed manually
