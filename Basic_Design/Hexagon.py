import turtle  # Import the turtle graphics module

# Set up the screen
screen = turtle.Screen()  # Create a screen object
screen.bgcolor("white")  # Set the background color of the screen to white
# screen.title("Python Turtle Graphics🐍🐢📊")  # Set the window title
screen.title("Hexagon Drawing")  # Set the title of the window to "Hexagon Drawing"

# Create the turtle
hex_turtle = turtle.Turtle()  # Create a turtle object named hex_turtle
hex_turtle.color("black")  # Set the turtle's pen color to black
hex_turtle.pensize(10)  # Set the pen size to 10 (thicker lines)
hex_turtle.speed(1)  # Set the turtle's drawing speed (1 = slow)

# Draw a hexagon in the center
side_length = 100  # Define the length of each side of the hexagon
angle = 60  # Define the turning angle for the hexagon (360/6 = 60 degrees)

# Move turtle to center starting position
hex_turtle.penup()  # Lift the pen so it doesn't draw while moving
hex_turtle.goto(-side_length / 2, -side_length / (2 * 3**0.5))  
hex_turtle.pendown()  # Put the pen down to start drawing

# Draw the hexagon
for _ in range(6):  # Repeat 6 times to draw 6 sides of a hexagon
    hex_turtle.forward(side_length)  # Move forward by side_length
    hex_turtle.left(angle)  # Turn left by the defined angle (60 degrees)

# Add text below the hexagon
hex_turtle.penup()
hex_turtle.goto(0, -side_length)  # Move to a position below the hexagon
hex_turtle.pendown()
hex_turtle.hideturtle()
hex_turtle.write("Hexagon", align="center", font=("Times New Roman", 18, "bold"))

# Keep the window open
screen.mainloop()
