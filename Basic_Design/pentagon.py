import turtle  # Import turtle graphics module for drawing
import math    # Import math module for mathematical functions

# Set up the screen
screen = turtle.Screen()          # Create a screen object where drawing happens
screen.title("Pentagon Drawing") # Set the window title

# Create turtle object
pen = turtle.Turtle()    # Create a turtle object named pen to draw with
pen.speed(3)             # Set drawing speed (1 slowest, 10 fastest)
pen.pensize(10)          # Set the thickness of the pen's drawing line
pen.hideturtle()         # Hide the turtle icon after drawing starts for cleaner look

# Pentagon parameters
side_length = 100            # Length of each side of the pentagon
num_sides = 5                # Number of sides in a pentagon
angle = 360 / num_sides      # Angle to turn after drawing each side (360 degrees divided equally)

# Calculate the radius of the circumscribed circle around the pentagon
radius = side_length / (2 * math.sin(math.pi / num_sides))  

# Calculate the starting point coordinates so the pentagon is centered at (0,0)
start_x = -side_length / 2 / math.tan(math.pi / num_sides)  # X coordinate of starting vertex
start_y = -radius * math.cos(math.pi / num_sides)           # Y coordinate of starting vertex

pen.up()                 # Lift pen to move without drawing
pen.goto(start_x, start_y) # Move turtle to calculated starting position
pen.setheading(0)         # Point the turtle to the right (0 degrees)
pen.down()                # Put pen down to start drawing

# Draw the pentagon by repeating forward and turn commands for each side
for _ in range(num_sides):
    pen.forward(side_length)  # Move forward by side length to draw a side
    pen.left(angle)           # Turn left by calculated angle to prepare for next side

# Write the text below the pentagon center
pen.up()                             # Lift pen to move without drawing
pen.goto(-20, start_y - 40)         # Move slightly below the pentagon for text placement
pen.write("Pentagon",                # Write the word "Pentagon"
          align="center",            # Center align the text at the turtle position
          font=("Times New Roman", 18, "bold"))  # Set font style, size, and weight

# Keep the window open until the user closes it
screen.mainloop()
