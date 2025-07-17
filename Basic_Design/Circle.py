import turtle  # Import the turtle graphics module

# Constants for the drawing
RADIUS = 100       # Radius of the circle to draw
PENSIZE = 10       # Thickness of the pen (line width)
TEXT_MARGIN = 30   # Extra space below the circle for placing the text label

# Set up the drawing screen/window
screen = turtle.Screen()        # Create a window for turtle graphics
screen.title("Circle Drawing")  # Set the window title
screen.bgcolor("white")         # Set background color of the window to white

# Create a turtle object to do the drawing
pen = turtle.Turtle()       # Instantiate a turtle pen
pen.hideturtle()            # Hide the turtle cursor (arrow) during drawing
pen.pensize(PENSIZE)        # Set the thickness of the pen's line
pen.speed(1)                # Set drawing speed (1 = slow, 10 = fast, 0 = instant)

# Prepare to draw the circle centered on the screen
pen.penup()                 # Lift the pen to move without drawing
pen.goto(0, -RADIUS)        # Move turtle to bottom edge of the circle (start point)
pen.pendown()               # Put the pen down to start drawing

# Draw the circle with specified radius
pen.circle(RADIUS)          # Draw a circle centered at (0,0) with radius RADIUS

# Calculate vertical position to place the text label below the circle
circle_height = 2 * RADIUS  # Diameter of the circle (height from top to bottom)

# Calculate y-coordinate for the text position:
# Start from center, move down half the circle height to bottom,
# adjust for pen thickness so text doesn't overlap the circle line,
# and add extra margin space to separate text visually.
text_y_offset = -circle_height / 2 - (PENSIZE / 2) - 2 * TEXT_MARGIN

# Move turtle to the position for writing the text label
pen.penup()                 # Lift pen to move without drawing
pen.goto(0, text_y_offset)  # Go to the center horizontally, and calculated y below circle
pen.pendown()               # Put pen down (not necessary here but consistent)

# Write the label text centered horizontally
pen.write("Circle", align="center", font=("Times New Roman", 18, "bold"))

# Finish turtle graphics and keep the window open
turtle.done()               # Keeps the window open until user closes it
