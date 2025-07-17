# Import the turtle graphics module
import turtle

# Set up the drawing screen
screen = turtle.Screen()          # Create a window for drawing
screen.bgcolor("white")           # Set the background color of the screen to white

# Create a turtle object that will draw the logo
logo = turtle.Turtle()            # Create a turtle named 'logo'
logo.shape("circle")              # Set the turtle's shape to a circle
logo.speed(5)                     # Set the drawing speed (1–10, with 10 being fastest)
logo.width(5)                     # Set the width of the lines the turtle draws

# Define a list of colors to use for the spiral logo
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']  # Colors for each spiral loop

# Define a function to draw the circular spiral logo using the colors
def draw_logo():
    for color in colors:         # Loop through each color in the colors list
        logo.color(color)        # Set the turtle's pen color
        logo.circle(100)         # Draw a circle with a radius of 100
        logo.right(60)           # Turn the turtle right by 60 degrees to create a spiral effect

# Define a function to draw the text below the logo
def draw_text():
    logo.penup()                 # Lift the pen so it doesn't draw while moving
    logo.goto(0, -250)           # Move the turtle to the position below the logo
    logo.pendown()               # Put the pen down to start drawing again
    logo.color("black")          # Set the pen color to black
    logo.write("Circle Design", align="center", font=("Arial", 24, "bold"))  # Write the label text

# Call the function to draw the logo
draw_logo()

# Call the function to draw the text below the logo
draw_text()

# Hide the turtle cursor after drawing is complete
logo.hideturtle()

# Keep the screen open until the user closes it manually
screen.mainloop()