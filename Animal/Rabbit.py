# Import the turtle graphics module
import turtle

# Setup the screen for drawing
screen = turtle.Screen()             # Create a window object
screen.bgcolor("lightblue")         # Set the background color of the window
screen.title("Cute Rabbit with Turtle")  # Set the title of the window

# Create the turtle object for drawing
rabbit = turtle.Turtle()            # Create a turtle named 'rabbit'
rabbit.speed(0)                     # Set the drawing speed to the fastest
rabbit.pensize(3)                   # Set the pen size (thickness of lines)
rabbit.hideturtle()                 # Hide the turtle cursor for clean drawing

# Function to draw a filled circle at (x, y) with specified radius and color
def draw_circle(x, y, radius, color):
    rabbit.penup()                          # Lift pen to move without drawing
    rabbit.goto(x, y - radius)             # Move to starting position (top of the circle)
    rabbit.pendown()                        # Put pen down to start drawing
    rabbit.color(color)                     # Set fill and pen color
    rabbit.begin_fill()                     # Begin the fill color
    rabbit.circle(radius)                   # Draw the circle
    rabbit.end_fill()                       # End the fill

# Function to draw an oval shape by combining two semicircles of different radii
def draw_oval(x, y, w, h, color):
    rabbit.penup()                          # Lift pen to move
    rabbit.goto(x, y)                       # Move to starting position
    rabbit.setheading(0)                    # Face the turtle to the right
    rabbit.pendown()                        # Put pen down to start drawing
    rabbit.color(color)                     # Set fill and pen color
    rabbit.begin_fill()                     # Start fill
    for i in range(2):                      # Repeat for two halves of the oval
        rabbit.circle(w, 90)                # Draw arc with radius 'w' and 90 degrees
        rabbit.circle(h, 90)                # Draw arc with radius 'h' and 90 degrees
    rabbit.end_fill()                       # End the fill

# Draw ears (white outer part)
draw_oval(-35, 100, 10, 30, "white")        # Left ear
draw_oval(35, 100, 10, 30, "white")         # Right ear

# Draw inner pink part of ears
draw_oval(-35, 110, 5, 20, "pink")          # Inner left ear
draw_oval(35, 110, 5, 20, "pink")           # Inner right ear

# Draw head
draw_circle(0, 50, 50, "white")             # Head centered at (0, 50)

# Draw eyes (white part)
draw_circle(-20, 80, 8, "white")            # Left eye white
draw_circle(20, 80, 8, "white")             # Right eye white

# Draw pupils (black part)
draw_circle(-20, 80, 3, "black")            # Left pupil
draw_circle(20, 80, 3, "black")             # Right pupil

# Draw nose
draw_circle(0, 65, 4, "pink")               # Pink nose at the center

# Draw cheeks
draw_circle(-35, 60, 6, "pink")             # Left cheek
draw_circle(35, 60, 6, "pink")              # Right cheek

# Draw body
draw_circle(0, -50, 70, "white")            # Large circle as body

# Draw feet (oval-shaped)
draw_oval(-40, -110, 10, 20, "white")       # Left foot
draw_oval(40, -110, 10, 20, "white")        # Right foot

# Add optional text below the rabbit
rabbit.penup()                              # Lift pen to move to text position
rabbit.goto(0, -180)                        # Move to bottom of screen
rabbit.color("black")                       # Set text color
rabbit.write("Cute Turtle Rabbit!",         # Text to display
             align="center",                # Centered alignment
             font=("Comic Sans MS", 16, "bold"))  # Font style

# Complete the drawing and wait for user to close the window
turtle.done()