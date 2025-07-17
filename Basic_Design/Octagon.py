import turtle  # Import the turtle graphics module to create drawings
import math    # Import the math module for mathematical functions like sine and cosine

# Set up the screen where the drawing will appear
screen = turtle.Screen()          # Create a new window for turtle graphics
screen.title("Octagon Drawing")  # Set the title of the window to "Octagon Drawing"

# Create the turtle pen that will draw the octagon
pen = turtle.Turtle()    # Initialize a turtle object to control drawing
pen.speed(3)             # Set drawing speed (1 is slowest, 10 is fastest)
pen.pensize(10)          # Set the thickness of the pen stroke to 10 pixels
pen.hideturtle()         # Hide the turtle icon (arrow) while drawing for a cleaner look

# Define parameters for the octagon shape
side_length = 100        # Each side of the octagon will be 100 units long
num_sides = 8            # Octagon has 8 sides
angle = 360 / num_sides  # Exterior angle to turn after each side to form the shape

# Calculate the radius of the circle that circumscribes the octagon
# This helps position the shape correctly on screen
radius = side_length / (2 * math.sin(math.pi / num_sides))
# Uses sine function and geometry to find radius from side length

# Calculate the approximate total horizontal width of the octagon
shape_width = 2 * radius  # Double the radius gives the diameter (width of the shape)

# Calculate how much to shift the starting position to center the octagon horizontally
shift_x = shape_width / 4  # Offset to adjust the octagon’s horizontal placement

# Calculate the x-coordinate to start drawing so the shape is centered
# Uses trigonometry to find position relative to the center
start_x = -side_length / 2 / math.tan(math.pi / num_sides) + shift_x

# Calculate the y-coordinate to start drawing so the shape is vertically aligned
start_y = -radius * math.cos(math.pi / num_sides)

# Move the pen to the starting position without drawing
pen.up()               # Lift pen so it does not draw while moving
pen.goto(start_x, start_y)  # Move pen to calculated start position
pen.setheading(0)      # Point pen to the right (0 degrees) to start drawing
pen.down()             # Put pen down to start drawing the octagon

# Draw the octagon by looping through each side
for _ in range(num_sides):   # Repeat 8 times (once per side)
    pen.forward(side_length) # Draw a side with length 100 units
    pen.left(angle)          # Turn left by the external angle to prepare for next side

# Position the pen below the octagon to write the label
pen.up()                     # Lift pen to move without drawing
pen.goto(-5, start_y - 40)   # Move to a point below the octagon for text

# Write the text "Octagon" centered horizontally below the shape
pen.write("Octagon",         # Text to display
          align="center",    # Center align the text horizontally
          font=("Times New Roman", 18, "bold"))  # Set font style, size, and weight

# Keep the turtle graphics window open until the user closes it manually
screen.mainloop()
