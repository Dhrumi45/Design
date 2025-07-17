import turtle  # Import the turtle graphics module

# Constants for the drawing
SQUARE_SIZE = 150         # Length of each side of the square
RECT_WIDTH = 250          # Width of the rectangle
RECT_HEIGHT = 150         # Height of the rectangle
PENSIZE = 10              # Thickness of the pen lines
TEXT_MARGIN = 30          # Vertical space between shape and its label text
SPACING = 50              # Horizontal space between the square and rectangle

# Setup screen
screen = turtle.Screen()              # Create a window for drawing
screen.title("Square and Rectangle Drawing")  # Set the window title
screen.bgcolor("white")               # Set the background color to white

pen = turtle.Turtle()                 # Create a turtle pen object to draw
pen.hideturtle()                     # Hide the turtle icon (arrow) during drawing
pen.pensize(PENSIZE)                 # Set the pen thickness
pen.speed(1)                        # Set drawing speed (1 = slow)

# Draw square on the left
# Calculate the center x-coordinate of the square, positioned left of center
square_center_x = -(RECT_WIDTH/2 + SPACING/2 + SQUARE_SIZE/2)
# Calculate bottom-left corner x-coordinate of the square from its center
square_bottom_left_x = square_center_x - SQUARE_SIZE/2
# Set bottom-left corner y-coordinate so the square is vertically centered at 0
square_bottom_left_y = -SQUARE_SIZE/2

pen.penup()                        # Lift pen to move without drawing
pen.goto(square_bottom_left_x, square_bottom_left_y)  # Move to square's bottom-left corner
pen.pendown()                      # Put pen down to start drawing
for _ in range(4):                 # Loop 4 times to draw 4 sides of the square
    pen.forward(SQUARE_SIZE)       # Draw one side of length SQUARE_SIZE
    pen.left(90)                   # Turn 90 degrees left to draw next side

# Write "Square" label below the square
pen.penup()                        # Lift pen to move without drawing
pen.goto(square_center_x, square_bottom_left_y - 2 * TEXT_MARGIN)  # Move below square for text
pen.pendown()                     # Put pen down (not really needed for write)
pen.write("Square", align="center", font=("Times New Roman", 18, "bold"))  # Write label centered

# Draw rectangle on the right
# Calculate the center x-coordinate of the rectangle, positioned right of center
rect_center_x = RECT_WIDTH/2 + SPACING/2 + SQUARE_SIZE/2
# Calculate bottom-left corner x-coordinate of the rectangle from its center
rect_bottom_left_x = rect_center_x - RECT_WIDTH/2
# Set bottom-left corner y-coordinate so the rectangle is vertically centered at 0
rect_bottom_left_y = -RECT_HEIGHT/2

pen.penup()                        # Lift pen to move without drawing
pen.goto(rect_bottom_left_x, rect_bottom_left_y)  # Move to rectangle's bottom-left corner
pen.pendown()                     # Put pen down to start drawing
for _ in range(2):                # Loop twice to draw the rectangle sides
    pen.forward(RECT_WIDTH)       # Draw the longer side (width)
    pen.left(90)                  # Turn 90 degrees left
    pen.forward(RECT_HEIGHT)      # Draw the shorter side (height)
    pen.left(90)                  # Turn 90 degrees left to prepare for next side

# Write "Rectangle" label below the rectangle
pen.penup()                      # Lift pen to move without drawing
pen.goto(rect_center_x, rect_bottom_left_y - 2 * TEXT_MARGIN)  # Move below rectangle for text
pen.pendown()                   # Put pen down (again, not necessary for writing)
pen.write("Rectangle", align="center", font=("Times New Roman", 18, "bold"))  # Write label

turtle.done()                   # Finish turtle graphics and keep window open
