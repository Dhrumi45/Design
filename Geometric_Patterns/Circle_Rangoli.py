import turtle  # Import turtle graphics module for drawing
import colorsys  # Import colorsys module to work with colors in HSV format

# Setup screen
screen = turtle.Screen()  # Create a screen/window for drawing
screen.bgcolor("black")  # Set the background color of the screen to black
screen.title("Circle-Only Rangoli (Filled + Outline)")  # Set the window title
turtle.colormode(1.0)  # Set color mode to 1.0 (allows RGB values between 0 and 1)

pen = turtle.Turtle()  # Create a turtle object called pen to draw with
pen.speed(0)  # Set drawing speed to fastest (0 is fastest)
pen.width(2)  # Set the pen width to 2 pixels
pen.hideturtle()  # Hide the turtle cursor for clean drawing

# Color palette
def generate_colors(n):
    # Generate a list of n colors evenly spaced in HSV hue, converted to RGB
    return [colorsys.hsv_to_rgb(i / n, 1.0, 1.0) for i in range(n)]

colors = generate_colors(100)  # Generate 100 colors for the palette

# Draw a filled circle with given radius and color
def draw_filled_circle(radius, color):
    pen.begin_fill()  # Start filling the shape with color
    pen.color(color)  # Set the pen color
    pen.circle(radius)  # Draw a circle with the specified radius
    pen.end_fill()  # Finish filling the shape

# Draw a circle outline (no fill) with given radius and color
def draw_outline_circle(radius, color):
    pen.color(color)  # Set the pen color
    pen.circle(radius)  # Draw a circle with the specified radius (outline only)

# Draw a ring of circles around the center
def draw_circle_ring(radius_from_center, count, circle_radius, filled=True, offset=0):
    for i in range(count):  # Loop to draw 'count' number of circles
        angle = 360 / count  # Calculate angle step between each circle
        pen.penup()  # Lift pen to move without drawing
        pen.goto(0, 0)  # Move to the center of the screen
        pen.setheading(angle * i + offset)  # Rotate pen to correct angle + optional offset
        pen.forward(radius_from_center)  # Move forward to the circle ring radius
        pen.setheading(0)  # Reset heading to the right (0 degrees)
        pen.pendown()  # Put pen down to start drawing
        color = colors[(i * 7) % len(colors)]  # Pick a color from the palette (patterned selection)
        if filled:
            pen.begin_fill()  # Start filling the circle if filled is True
            pen.color(color)  # Set pen color
            pen.circle(circle_radius)  # Draw the circle with given radius
            pen.end_fill()  # End fill
        else:
            pen.color(color)  # Set pen color
            pen.circle(circle_radius)  # Draw circle outline without fill

# === Center Concentric Circles ===
pen.penup()  # Lift pen to move without drawing
pen.goto(0, -20)  # Move to position below the center (circle will be drawn upwards)
pen.pendown()  # Put pen down to draw
draw_filled_circle(20, "white")  # Draw a filled white circle with radius 20 at center

pen.penup()  # Lift pen again
pen.goto(0, -30)  # Move slightly further down for next circle
pen.pendown()  # Put pen down to draw
draw_outline_circle(30, "white")  # Draw a white outline circle with radius 30

# === Circle Rings ===
draw_circle_ring(radius_from_center=60, count=12, circle_radius=10, filled=True)  # Inner filled ring
draw_circle_ring(radius_from_center=100, count=16, circle_radius=15, filled=False, offset=12)  # Outline ring with offset
draw_circle_ring(radius_from_center=150, count=20, circle_radius=8, filled=True)  # Filled ring farther out
draw_circle_ring(radius_from_center=190, count=24, circle_radius=12, filled=False, offset=8)  # Outline ring with offset

# === Outer Dot Ring ===
draw_circle_ring(radius_from_center=230, count=30, circle_radius=5, filled=True)  # Small filled dots in outermost ring

turtle.done()  # Finish drawing and keep window open
