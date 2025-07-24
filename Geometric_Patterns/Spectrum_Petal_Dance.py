import turtle
import colorsys

# Setup screen
screen = turtle.Screen()             # Create a screen object
screen.bgcolor("black")              # Set the background color of the screen to black
screen.title("Authentic Rangoli Design")  # Set the title of the turtle graphics window
turtle.colormode(1.0)                # Set color mode to 1.0 (RGB values between 0 and 1)

# Create turtle pen
pen = turtle.Turtle()               # Create a turtle object named 'pen'
pen.speed(0)                        # Set turtle speed to maximum
pen.width(2)                        # Set the width of the pen
pen.hideturtle()                    # Hide the turtle icon for clean drawing

# Generate rainbow colors using HSV color space
def generate_colors(n):
    return [colorsys.hsv_to_rgb(i/n, 1.0, 1.0) for i in range(n)]  # Generate 'n' distinct HSV colors and convert to RGB

colors = generate_colors(100)       # Generate a list of 100 rainbow colors

# Function to draw a petal using arc shapes
def draw_petal(radius, angle):
    for _ in range(2):              # Each petal is made of 2 arcs
        pen.circle(radius, angle)   # Draw an arc of specified radius and angle
        pen.left(180 - angle)       # Turn left to mirror the arc and form a petal

# Function to draw a complete flower with multiple petals
def draw_flower(petals, radius, angle, size):
    for i in range(petals):                         # Loop through each petal
        pen.color(colors[i % len(colors)])          # Pick a color cyclically from the color list
        pen.begin_fill()                            # Start filling the petal
        draw_petal(size, angle)                     # Draw the petal
        pen.end_fill()                              # End the fill
        pen.left(360 / petals)                      # Rotate to the position for next petal

# Function to draw circular layers made of arc petals
def draw_arc_circle(radius, count, arc_angle=60):
    for i in range(count):                          # Loop for each arc
        pen.penup()                                 # Lift pen to reposition
        pen.goto(0, -radius)                        # Move to starting position
        pen.setheading(i * (360 / count))           # Set heading angle for each arc
        pen.pendown()                               # Put pen down to start drawing
        pen.color(colors[i % len(colors)])          # Select color
        pen.begin_fill()                            # Start fill for arc shape
        pen.circle(radius, arc_angle)               # Draw first arc
        pen.left(180 - arc_angle)                   # Rotate for second arc to complete petal
        pen.circle(radius, arc_angle)               # Draw second arc
        pen.end_fill()                              # End fill

# Draw the central white circle
pen.penup()                    # Lift the pen
pen.goto(0, -20)               # Move to center bottom of the circle
pen.pendown()                  # Put the pen down
pen.color("white")            # Set color to white
pen.begin_fill()               # Start filling the circle
pen.circle(20)                 # Draw a circle of radius 20
pen.end_fill()                 # End fill

# First layer: Flower with 8 petals
pen.penup()                    # Lift pen before repositioning
pen.goto(0, 0)                 # Move to center
pen.setheading(0)              # Face right (0 degrees)
pen.pendown()                  # Put pen down
draw_flower(petals=8, radius=60, angle=60, size=60)  # Draw flower

# Second layer (optional): Circular arc petals
# Uncomment below to include it
# draw_arc_circle(radius=90, count=12)

# Third layer: Draw a flower using square shapes at the edge of a circle
def draw_square_flower(radius, size):
    for i in range(8):                             # Loop through 8 square petals
        angle = 360 / 8                            # Calculate angle step
        pen.penup()                                # Lift pen
        pen.goto(0, 0)                             # Move to center
        pen.setheading(angle * i)                  # Set direction outward
        pen.forward(radius)                        # Move to radius distance
        pen.pendown()                              # Start drawing
        pen.setheading(angle * i + 45)             # Rotate square for better shape
        pen.color(colors[(i * 7) % len(colors)])   # Pick color with some offset
        pen.begin_fill()                           # Start fill
        for _ in range(4):                         # Draw a square
            pen.forward(size)
            pen.right(90)
        pen.end_fill()                             # End fill

draw_square_flower(radius=130, size=40)            # Draw the square flower layer

# Final outer circle made of colorful dots
def draw_outer_dots(radius, count):
    for i in range(count):                          # Loop for each dot
        angle = 360 / count                         # Compute angle for each dot
        pen.penup()                                 # Lift pen
        pen.goto(0, 0)                              # Move to center
        pen.setheading(angle * i)                   # Set heading angle
        pen.forward(radius)                         # Move to outer position
        pen.pendown()                               # Start drawing
        pen.color(colors[i % len(colors)])          # Select a color
        pen.begin_fill()                            # Begin fill
        pen.circle(8)                               # Draw small dot circle
        pen.end_fill()                              # End fill

draw_outer_dots(radius=200, count=24)              # Draw 24 colorful dots around

turtle.done()                                       # Finish turtle graphics and keep window open
