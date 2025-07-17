import turtle  # Import the turtle graphics module for drawing shapes

# Constants for the drawing
BASE_HEIGHT = 150  # Base height used as a reference for sizing the triangle (original was around 200)
SCALE_FACTOR = 2   # Factor to scale the triangle size (2 means double the base size)
# Calculate the side length of the equilateral triangle scaled up by SCALE_FACTOR
SIDE_LENGTH = SCALE_FACTOR * (2 * BASE_HEIGHT * 3**0.5 / 3)  
PENSIZE = 10       # Thickness of the lines drawn by the turtle pen
TEXT_MARGIN = 30   # Extra space below the triangle to place the text label without overlapping

# Set up the drawing screen/window
screen = turtle.Screen()        # Create a window for turtle graphics to appear
screen.title("Triangle Drawing")  # Set the title of the turtle graphics window
screen.bgcolor("white")         # Set the background color of the window to white

# Create a turtle object to do the drawing
pen = turtle.Turtle()       # Instantiate a turtle object (pen) to draw with
pen.hideturtle()            # Hide the turtle cursor so only lines are visible
pen.pensize(PENSIZE)        # Set the width of the lines the pen will draw
pen.speed(1)                # Set the speed of drawing (1 = slowest animation)

# Calculate the height of the equilateral triangle using the formula: height = (sqrt(3)/2)*side
triangle_height = (3**0.5 / 2) * SIDE_LENGTH  

# Prepare to draw the triangle centered on the screen
pen.penup()  # Lift the pen so it doesn’t draw while moving to start position
# Move the pen to the bottom left vertex of the triangle to start drawing
pen.goto(-SIDE_LENGTH / 2, -triangle_height / 2)  
pen.pendown()  # Put the pen down to start drawing

# Draw an equilateral triangle by repeating move forward and turn left 120 degrees three times
for _ in range(3):
    pen.forward(SIDE_LENGTH)  # Draw one side of the triangle
    pen.left(120)             # Turn left 120 degrees to prepare for the next side

# Calculate the vertical position for the text below the triangle, accounting for pen size and margin
text_y_offset = -triangle_height / 2 - (PENSIZE / 2) - 2 * TEXT_MARGIN

# Move the turtle to the position for writing the text label below the triangle
pen.penup()  # Lift pen to move without drawing
pen.goto(0, text_y_offset)  # Go to horizontal center and calculated vertical offset
pen.pendown()  # Pen down to write the text

# Write the label "Triangle" centered horizontally with specified font style and size
pen.write("Triangle", align="center", font=("Times New Roman", 18, "bold"))

# Finish turtle graphics drawing and keep the window open until manually closed
turtle.done()
