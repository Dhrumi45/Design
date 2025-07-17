import turtle  # Import the turtle graphics module

# Set up the screen
screen = turtle.Screen()  # Create a screen object
screen.bgcolor("white")  # Set the background color of the screen to white
screen.title("Hexagon with Extended Lines")  # Set the window title

# Create the turtle
hex_turtle = turtle.Turtle()  # Create a turtle named hex_turtle
hex_turtle.color("black")  # Set the pen color to black
hex_turtle.pensize(10)  # Set the pen size to 10 for thick lines
hex_turtle.speed(1)  # Set drawing speed (1 = slowest)

# Parameters
side_length = 60  # Length of each side of the hexagon
angle = 60  # Turning angle for each corner of the hexagon
extension_length = 60  # Length of the extension after each side
perpendicular_length = extension_length  # Length of perpendicular outward line

# Move turtle to center starting position
hex_turtle.penup()  # Lift the pen to move without drawing
# Move to a starting point adjusted so the hexagon is centered
hex_turtle.goto(-side_length / 2, -side_length / (2 * 3**0.5))
hex_turtle.setheading(0)  # Set turtle facing right (0 degrees)
hex_turtle.pendown()  # Put the pen down to start drawing

# Draw the hexagon with extensions and perpendicular lines
for _ in range(6):  # Repeat for 6 sides of the hexagon
    hex_turtle.forward(side_length)  # Draw one side of the hexagon

    hex_turtle.forward(extension_length)  # Continue drawing the extension line

    hex_turtle.left(60)  # Turn left to draw a perpendicular line (outward)
    hex_turtle.forward(perpendicular_length)  # Draw the perpendicular outward line
    hex_turtle.backward(perpendicular_length)  # Move back to the previous position

    hex_turtle.right(60)  # Turn back to original direction
    hex_turtle.penup()  # Lift the pen to move without drawing
    hex_turtle.backward(extension_length)  # Go back to the end of the hexagon side

    hex_turtle.left(angle)  # Turn left to get ready for the next side of the hexagon
    hex_turtle.pendown()  # Put the pen down to draw the next side

# Hide the turtle and keep the window open
hex_turtle.hideturtle()  # Hide the turtle cursor

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
hex_turtle.write("Hexagon with two parallel extended side", align="center", font=("Times New Roman", 18, "bold"))

screen.mainloop()  # Keep the window open until manually closed
