import turtle  # Import the turtle graphics module to create drawings
import math    # Import the math module for mathematical functions like sine and cosine

# Set up the screen where the drawing will appear
screen = turtle.Screen()          # Create a new window for turtle graphics
screen.title("Nonagon Drawing")  # Set the title of the window to "Nonagon Drawing"

# Create the turtle pen that will draw the nonagon
pen = turtle.Turtle()    # Initialize a turtle object to control drawing
pen.speed(3)             # Set drawing speed (1 is slowest, 10 is fastest)
pen.pensize(10)          # Set the thickness of the pen stroke to 10 pixels
pen.hideturtle()         # Hide the turtle icon (arrow) while drawing for a cleaner look

# Define parameters for the nonagon shape
side_length = 100        # Length of each side of the nonagon
num_sides = 9            # Total number of sides for a nonagon
angle = 360 / num_sides  # Exterior angle to turn the pen after drawing each side

# Calculate the radius of the circle that perfectly fits around the nonagon
radius = side_length / (2 * math.sin(math.pi / num_sides))  # Using trigonometry to compute radius

# Calculate the total approximate horizontal width of the nonagon
shape_width = 2 * radius  # Width from leftmost to rightmost point of the circumscribed circle

# Determine how much to shift the starting point on the x-axis to center the nonagon
shift_x = shape_width / 4  # A quarter of the shape's width to slightly adjust the position

# Compute the x-coordinate for the starting point so that drawing appears centered
start_x = -side_length / 2 / math.tan(math.pi / num_sides) + shift_x  # Align horizontally

# Compute the y-coordinate for the starting point so the shape is vertically balanced
start_y = -radius * math.cos(math.pi / num_sides)  # Slightly shift downward to make room for label

# Move the turtle pen to the starting position without drawing a line
pen.up()                 # Lift the pen up to prevent drawing while moving
pen.goto(start_x, start_y)  # Go to the calculated start position
pen.setheading(0)        # Set the initial heading angle (facing right)
pen.down()               # Put the pen down to begin drawing

# Draw the nonagon by repeating forward and turn for each side
for _ in range(num_sides):  # Repeat for each of the 9 sides
    pen.forward(side_length)  # Move forward by the length of one side
    pen.left(angle)           # Turn left by the calculated exterior angle

# Move the pen below the nonagon to place a label
pen.up()                          # Lift the pen to move without drawing
pen.goto(-14, start_y - 40)       # Position slightly below the shape for the label

# Write "Nonagon" below the drawn shape with specified style
pen.write("Nonagon",              # Text to write
          align="center",         # Center the text horizontally
          font=("Times New Roman", 18, "bold"))  # Font type, size, and style

# Keep the turtle graphics window open until it is manually closed
screen.mainloop()  # Enter the event loop to keep window displayed
