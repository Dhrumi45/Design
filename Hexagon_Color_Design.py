import turtle  # Import the turtle graphics library for drawing shapes

# Set up the screen
screen = turtle.Screen()  # Create a drawing window (screen) object
screen.bgcolor("white")  # Set the background color of the screen to white
screen.title("Hexagon with Colored Triangles")  # Set the title of the drawing window

# Create the turtle (drawing pen)
hex_turtle = turtle.Turtle()  # Instantiate a turtle object to control drawing
hex_turtle.pensize(10)   # Set the thickness of the pen lines to 10 pixels (bold lines)
hex_turtle.speed(3)  # Set drawing speed; 3 is a moderate speed

# Define parameters for the hexagon and triangles
side_length = 100  # Length of each side of the hexagon
angle = 60  # The angle the turtle turns at each corner (hexagon internal angle)
extension_length = 100  # Distance the triangle extends outward from each hex side
perpendicular_length = 2 * extension_length  # Height of the triangle, perpendicular to the hex side

# List of colors for filling each triangle outside the hexagon
colors = ["red", "green", "blue", "orange", "purple", "yellow"]

# Position the turtle to start drawing the hexagon centered on the screen
hex_turtle.penup()  # Lift the pen so no drawing occurs during movement
# Calculate starting coordinates to center hexagon roughly on screen
hex_turtle.goto(-side_length / 2, -side_length / (2 * 3**0.5))
hex_turtle.setheading(0)  # Point the turtle to the right (east)
hex_turtle.pendown()  # Place the pen down to start drawing

# Loop through each of the 6 sides of the hexagon
for i in range(6):
    hex_turtle.color("black")  # Set the pen color to black for the hexagon sides
    hex_turtle.forward(side_length)  # Draw one side of the hexagon

    # Save the current position and direction before drawing the triangle
    pos = hex_turtle.pos()  # Store the (x, y) position of the turtle
    heading = hex_turtle.heading()  # Store the current heading angle of the turtle

    # Start drawing the colored triangle attached to the hexagon side
    hex_turtle.fillcolor(colors[i])  # Set the fill color for the triangle
    hex_turtle.begin_fill()  # Start the fill process

    hex_turtle.forward(extension_length)  # Move forward beyond the hex side to draw triangle
    hex_turtle.left(90)  # Turn left 90 degrees to draw the perpendicular side of the triangle
    hex_turtle.forward(perpendicular_length)  # Draw the height of the triangle
    hex_turtle.right(135)  # Turn right 135 degrees to face back towards the start point
    hex_turtle.goto(pos)  # Move turtle back to the starting point of the hex side (close triangle)

    hex_turtle.end_fill()  # Complete filling the triangle with the chosen color

    # Reset the turtle's heading and position to continue drawing the hexagon
    hex_turtle.setheading(heading)  # Restore the turtle's original direction
    hex_turtle.penup()  # Lift the pen to move without drawing
    hex_turtle.goto(pos)  # Return to the end of the hexagon side
    hex_turtle.pendown()  # Place the pen down to draw the next side

    hex_turtle.left(angle)  # Turn left 60 degrees to prepare for next hexagon side

# Hide the turtle cursor once drawing is complete
hex_turtle.hideturtle()

# Write a centered label below the drawing
hex_turtle.penup()  # Lift the pen to move without drawing
hex_turtle.goto(0, -side_length * 2.5)  # Move turtle downward to position text below design
hex_turtle.color("black")  # Set pen color to black for the text
# Write the text centered with specified font style and size
hex_turtle.write("Hexagon & Triangle Design", align="center", font=("Times New Roman", 18, "bold"))

# Keep the window open until the user closes it
screen.mainloop()