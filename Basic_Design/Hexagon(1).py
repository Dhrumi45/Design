import turtle  # Import the turtle graphics module

# Set up the screen
screen = turtle.Screen()              # Create a screen object
screen.bgcolor("white")               # Set background color to white
screen.title("Hexagon with Extended Lines")  # Set the window title

# Create the turtle
hex_turtle = turtle.Turtle()          # Create a turtle object named 'hex_turtle'
hex_turtle.color("black")             # Set the pen color to black
hex_turtle.pensize(10)                # Set the thickness of the pen to 10
hex_turtle.speed(1)                   # Set turtle drawing speed (1 is slowest)

# Parameters
side_length = 50                      # Length of each side of the hexagon
angle = 60                            # Interior angle to turn for a hexagon
extension_length = 60                 # Extra length to draw beyond each hexagon side

# Move turtle to center starting position
hex_turtle.penup()                    # Lift the pen to move without drawing
hex_turtle.goto(-side_length / 2, -side_length / (2 * 3**0.5))  # Position turtle so hexagon is centered
hex_turtle.setheading(0)             # Set turtle's direction to the right (0 degrees)
hex_turtle.pendown()                 # Put the pen down to start drawing

# Draw the hexagon and extend each side in the same direction
for _ in range(6):                    # Repeat 6 times for 6 sides of a hexagon
    hex_turtle.forward(side_length)  # Draw one side of the hexagon

    hex_turtle.forward(extension_length)  # Extend line beyond the side

    hex_turtle.penup()                   # Lift pen to move back without drawing
    hex_turtle.backward(extension_length)  # Move back to the corner of the hexagon side

    hex_turtle.left(angle)               # Turn left by 60 degrees to face next side
    hex_turtle.pendown()                 # Put pen down to draw the next side

# Hide the turtle and keep the window open
hex_turtle.hideturtle()              # Hide the turtle cursor from view

# Add text below the hexagon
# Calculate appropriate Y-position for text
# Height of hexagon = side_length * sqrt(3)
# Calculate the height of the hexagon using the formula: side * sqrt(3)
hex_height = side_length * (3**0.5)

# Calculate the Y position for the text so it appears below the extended part of the hexagon
# We move down by half the hexagon height, then by the extension length, and finally by 30 units as extra margin
text_y_offset = -hex_height / 2 - extension_length - 30  # Adjust -30 for margin

# Lift the pen up to move the turtle without drawing
hex_turtle.penup()

# Move the turtle to the X-center (0) and the calculated Y position for the text
hex_turtle.goto(0, text_y_offset)

# Put the pen down to prepare for writing text
hex_turtle.pendown()

# Write the text centered at the current turtle position with the specified font
hex_turtle.write("Hexagon with one extended side", align="center", font=("Times New Roman", 18, "bold"))


screen.mainloop()                    # Keep the window open until closed manually

