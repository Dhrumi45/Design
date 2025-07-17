# Import the turtle module for drawing
import turtle

# Set up the drawing screen
screen = turtle.Screen()                # Create a screen object
screen.bgcolor("lightyellow")           # Set the background color of the screen
screen.title("Cute Cat Drawing")        # Set the title of the window

# Create a turtle object to draw the cat
cat = turtle.Turtle()                   # Create a turtle named 'cat'
cat.speed(0)                            # Set the fastest drawing speed
cat.pensize(2)                          # Set the pen thickness to 2
cat.hideturtle()                        # Hide the turtle cursor for clean drawing

# Function to draw a filled circle
def draw_circle(x, y, radius, color):
    cat.penup()                         # Lift the pen to move without drawing
    cat.goto(x, y - radius)             # Move to the starting point (top of circle)
    cat.pendown()                       # Put the pen down to start drawing
    cat.color(color)                    # Set the color for the circle
    cat.begin_fill()                    # Start filling the shape with color
    cat.circle(radius)                  # Draw a circle with the given radius
    cat.end_fill()                      # End the filling process

# Function to draw a filled triangle (used for ears)
def draw_triangle(x, y, size, color):
    cat.penup()                         # Lift the pen to move
    cat.goto(x, y)                      # Move to starting point of triangle
    cat.setheading(0)                   # Set the drawing angle to the right (0 degrees)
    cat.pendown()                       # Put the pen down to draw
    cat.color(color)                    # Set the fill color
    cat.begin_fill()                    # Start filling the shape
    for _ in range(3):                  # Loop to draw 3 sides of triangle
        cat.forward(size)              # Draw one side of the triangle
        cat.left(120)                  # Turn left 120 degrees to make an equilateral triangle
    cat.end_fill()                      # End the fill

# === Drawing the Ears ===
draw_triangle(-60, 100, 40, "gray")     # Draw left ear
draw_triangle(20, 100, 40, "gray")      # Draw right ear

# === Drawing the Inner Ears ===
draw_triangle(-50, 110, 20, "pink")     # Draw inner part of left ear
draw_triangle(30, 110, 20, "pink")      # Draw inner part of right ear

# === Drawing the Head ===
draw_circle(0, 60, 60, "gray")          # Draw the head as a large circle

# === Drawing the Eyes ===
draw_circle(-20, 90, 10, "white")       # Left white part of eye
draw_circle(20, 90, 10, "white")        # Right white part of eye
draw_circle(-20, 90, 4, "black")        # Left pupil
draw_circle(20, 90, 4, "black")         # Right pupil

# === Drawing the Nose ===
draw_circle(0, 70, 5, "pink")           # Nose at the center

# === Drawing the Mouth ===
cat.penup()
cat.goto(-5, 65)                        # Move to left side of mouth
cat.setheading(-30)                     # Set angle to draw left smile curve
cat.pendown()
cat.circle(10, 60)                      # Draw left curve of mouth

cat.penup()
cat.goto(5, 65)                         # Move to right side of mouth
cat.setheading(-150)                    # Set angle to draw right smile curve
cat.pendown()
cat.circle(-10, 60)                     # Draw right curve of mouth

# === Drawing the Whiskers ===
cat.color("black")                      # Set pen color to black
for y in [70, 75, 65]:                  # Loop over 3 vertical positions for whiskers
    for direction in [-1, 1]:           # Loop to draw left and right whiskers
        cat.penup()
        cat.goto(0, y)                  # Start from center of face at given height
        cat.setheading(0)               # Face right
        cat.pendown()
        cat.forward(40 * direction)     # Draw whisker line to left (-1) or right (1)

# === Drawing the Body ===
draw_circle(0, -50, 80, "gray")         # Draw large body below head

# === Drawing the Paws ===
draw_circle(-40, -120, 20, "gray")      # Left paw
draw_circle(40, -120, 20, "gray")       # Right paw

# === Drawing the Tail ===
cat.penup()
cat.goto(60, -130)                      # Starting point of tail
cat.pendown()
cat.pensize(4)                          # Thicker pen for the tail
cat.color("gray")                       # Tail color
cat.setheading(-60)                     # Angle to start the curve
for i in range(70):                     # Loop to draw a spiral tail
    cat.forward(2)                      # Move forward slightly
    cat.left(2)                         # Turn left gradually to create curve

# === Writing Text ===
cat.penup()
cat.goto(0, -210)                       # Move to bottom of screen
cat.color("black")                      # Text color
cat.write("Meow! I'm a Cat 🐱",         # Message to display
          align="center", 
          font=("Times New Roman", 18, "bold"))   # Font styling

# End the turtle graphics and keep the window open
turtle.done()