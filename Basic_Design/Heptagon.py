import turtle  # Import the turtle graphics module
import math    # Import the math module for mathematical functions

# Set up the screen
screen = turtle.Screen()          # Create a screen object for drawing
screen.title("Heptagon Drawing")  # Set the window title

# Create turtle object
pen = turtle.Turtle()    # Create a turtle pen object for drawing
pen.speed(3)             # Set the drawing speed (1 slowest, 10 fastest)
pen.pensize(10)          # Set the thickness of the pen stroke
pen.hideturtle()         # Hide the turtle icon (arrow) after setup

# Heptagon parameters
side_length = 100        # Length of each side of the heptagon
num_sides = 7            # Number of sides in a heptagon
angle = 360 / num_sides  # External turning angle for each vertex

# Calculate radius of circumscribed circle for heptagon
radius = side_length / (2 * math.sin(math.pi / num_sides))  
# Calculate radius of circle circumscribing the heptagon using trigonometry

# Calculate the width of the heptagon (approximate horizontal span)
# The width is roughly twice the radius since the shape is inscribed in a circle
shape_width = 2 * radius  # Total horizontal span across the heptagon

# Calculate starting position to center the heptagon horizontally around 0,
# then shift it right by half the width to center both shape and text
shift_x = shape_width / 4  # Horizontal offset to better center the shape

start_x = -side_length / 2 / math.tan(math.pi / num_sides) + shift_x  
# Calculate the x-coordinate of the starting position based on geometry

start_y = -radius * math.cos(math.pi / num_sides)  
# Calculate the y-coordinate of the starting position to align vertically

pen.up()               # Lift the pen so it doesn't draw when moving
pen.goto(start_x, start_y)  # Move turtle to the calculated starting point
pen.setheading(0)      # Set the initial direction facing right (0 degrees)
pen.down()             # Put the pen down to start drawing

# Draw the heptagon
for _ in range(num_sides):   # Loop through each side of the heptagon
    pen.forward(side_length) # Draw one side of the heptagon
    pen.left(angle)          # Turn the turtle left by the external angle

# Write the text below the shape aligned horizontally with the shape center
pen.up()                     # Lift pen to move without drawing
pen.goto(5, start_y - 40)    # Move below the heptagon for text placement
pen.write("Heptagon",        # Write the label "Heptagon"
          align="center",    # Center the text horizontally
          font=("Times New Roman", 18, "bold"))  # Set font style and size

screen.mainloop()            # Keep the window open until closed by the user
