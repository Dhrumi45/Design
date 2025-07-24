import turtle                      # Import turtle graphics module for drawing
import colorsys                    # Import colorsys to handle color conversions (HSV to RGB)

# Setup screen
screen = turtle.Screen()          # Create a window for drawing
screen.bgcolor("black")           # Set background color of the window to black
screen.title("Triangle-Only Rangoli")  # Set the title of the window
turtle.colormode(1.0)             # Use float RGB color mode where colors range from 0.0 to 1.0

# Create drawing turtle
pen = turtle.Turtle()             # Create a turtle object to draw shapes
pen.speed(0)                     # Set drawing speed to fastest (0 means no animation delay)
pen.width(2)                     # Set the pen thickness to 2 pixels
pen.hideturtle()                 # Hide the turtle pointer to just see the drawing

# Generate smooth rainbow colors
def generate_colors(n):
    # Return a list of n colors evenly spaced in HSV hue, converted to RGB
    return [colorsys.hsv_to_rgb(i / n, 1.0, 1.0) for i in range(n)]

colors = generate_colors(100)    # Generate 100 colors to use for filling triangles

# Function to draw a triangle of given size
def draw_triangle(size):
    for _ in range(3):           # Loop 3 times for 3 sides
        pen.forward(size)        # Move pen forward by 'size' pixels
        pen.left(120)            # Turn pen left by 120 degrees to form triangle angles

# Function to draw a ring of triangles around the center
def draw_triangle_ring(radius, count, size, rotation_offset=0):
    for i in range(count):       # Repeat 'count' times to draw 'count' triangles
        angle = 360 / count      # Calculate angle between each triangle in the ring
        pen.penup()              # Lift pen to move without drawing
        pen.goto(0, 0)           # Move pen to center of screen
        pen.setheading(angle * i + rotation_offset)  # Point pen in correct direction for this triangle
        pen.forward(radius)      # Move pen outward by 'radius' to position triangle
        pen.pendown()            # Put pen down to start drawing
        pen.setheading(angle * i + rotation_offset)  # Ensure heading is still correct before drawing
        pen.color(colors[(i * 7) % len(colors)])  # Set pen color cycling through the generated colors
        pen.begin_fill()         # Start filling shape with color
        draw_triangle(size)      # Draw a single triangle of given size
        pen.end_fill()           # Complete fill of triangle

# Draw multiple rings of triangles with different sizes, counts, and rotations
draw_triangle_ring(radius=80, count=12, size=60)                   # First ring of 12 triangles at radius 80
draw_triangle_ring(radius=140, count=18, size=50, rotation_offset=10)  # Second ring of 18 triangles rotated 10°
draw_triangle_ring(radius=200, count=24, size=40, rotation_offset=20)  # Third ring of 24 triangles rotated 20°

# Draw a small flower of triangles in the center
pen.penup()                       # Lift pen up to move without drawing
pen.goto(0, 0)                   # Go to center
pen.setheading(0)                # Set heading to 0 degrees (pointing right)
pen.pendown()                   # Pen down to draw
draw_triangle_ring(radius=30, count=6, size=30)   # Draw 6 small triangles at center radius 30

# Draw outer tiny decorative ring of triangles
draw_triangle_ring(radius=260, count=30, size=20, rotation_offset=15)  # Draw 30 tiny triangles in outer ring

turtle.done()                   # Finish drawing and keep the window open until closed by user
