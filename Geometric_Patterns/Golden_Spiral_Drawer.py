# Import necessary libraries
import turtle                     # Turtle graphics for drawing
import colorsys                   # Colorsys module to convert HSV to RGB
from math import pi, sqrt, sin, cos  # Import mathematical constants and functions

# Function to draw an equilateral triangle
def draw_triangle(size=8):
    """Draws an equilateral triangle centered at the current turtle position."""
    turtle.begin_fill()          # Start filling the shape with color
    for _ in range(3):           # Repeat 3 times for triangle sides
        turtle.forward(size)     # Move forward by 'size' units
        turtle.left(120)         # Turn left by 120° to form triangle angle
    turtle.end_fill()            # End filling the shape

# Function to draw a diamond shape (rhombus)
def draw_diamond(size=8):
    """Draws a diamond (rhombus) shape centered at the current turtle position."""
    turtle.begin_fill()          # Start filling the shape
    for _ in range(2):           # Repeat 2 times (each loop draws half the diamond)
        turtle.forward(size)     # Move forward by 'size' units
        turtle.left(60)          # Turn left 60°
        turtle.forward(size)     # Move forward again
        turtle.left(120)         # Turn left 120° to form diamond angle
    turtle.end_fill()            # End filling

# Function to draw a small filled circle
def draw_circle(radius=4):
    """Draws a filled circle centered at the current turtle position."""
    turtle.begin_fill()          # Start filling
    turtle.circle(radius)        # Draw circle of given radius
    turtle.end_fill()            # End filling

# Function to generate a colorful spiral pattern
def generate_spiral(
    total_dots=5000,                              # Number of shapes to draw
    golden_angle=2 * pi / ((1 + sqrt(5)) / 2),    # Angle between shapes (golden angle)
    spacing=2.0,                                  # Distance between spiral arms
    center=(0, 0),                                # Center point of spiral
    shape_type="circle"                           # Type of shape: triangle, diamond, or circle
):
    """
    Draws a colorful spiral pattern using turtle graphics.
    """
    
    screen = turtle.Screen()                      # Create turtle screen
    screen.setup(width=1.0, height=1.0)           # Maximize screen size
    screen.title("Spiral Pattern with Custom Shapes")  # Set window title

    turtle.hideturtle()                           # Hide turtle cursor for clean drawing
    turtle.speed(0)                               # Set turtle to fastest speed
    turtle.penup()                                # Lift pen to avoid drawing lines between moves
    turtle.delay(0)                               # Remove delay between turtle moves

    # Loop to draw all dots/shapes
    for i in range(total_dots):
        angle = golden_angle * i                  # Compute angle using golden angle
        radius = spacing * sqrt(angle)            # Compute radius for current point
        x = center[0] + radius * cos(angle)       # Compute x position
        y = center[1] + radius * sin(angle)       # Compute y position

        hue = i / total_dots                      # Normalize hue between 0 and 1
        r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)  # Convert HSV to RGB color

        turtle.goto(x, y)                          # Move turtle to computed position
        turtle.setheading(angle * 180 / pi)        # Point turtle in direction of angle
        turtle.color(r, g, b)                      # Set pen color
        turtle.pendown()                           # Put pen down to start drawing

        # Choose and draw the shape based on shape_type
        if shape_type == "triangle":
            draw_triangle(size=6)                  # Draw triangle
        elif shape_type == "diamond":
            draw_diamond(size=6)                   # Draw diamond
        elif shape_type == "circle":
            draw_circle(radius=2)                  # Draw small circle

        turtle.penup()                              # Lift pen to move without drawing

    turtle.exitonclick()                            # Wait for user click to close window

# Main block to run when script is executed directly
if __name__ == "__main__":
    # Call the spiral generation with shape_type set to "circle"
    generate_spiral(shape_type="circle")
