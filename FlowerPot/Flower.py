import turtle  # Import the turtle graphics module

# Set up the screen
screen = turtle.Screen()       # Create a screen window
screen.bgcolor("white")        # Set background color to white
screen.title("8-Petal Flower") # Set the title of the window

# Create the turtle
flower = turtle.Turtle()       # Create a turtle object named 'flower'
flower.shape("turtle")         # Set turtle shape to 'turtle'
flower.color("red")            # Set pen color to red
flower.pensize(2)              # Set the pen thickness to 2
flower.speed(6)                # Set the turtle drawing speed (1-10 scale)

# Petal drawing function
def draw_petal():
    for _ in range(2):                     # Repeat twice to make both halves of the petal
        flower.circle(100, 60)             # Draw an arc with radius 100 and angle 60 degrees
        flower.left(120)                   # Turn left by 120 degrees to draw the other side

# Draw 8 petals
for _ in range(8):              # Repeat 8 times to make 8 petals
    draw_petal()                # Call the function to draw one petal
    flower.left(45)             # Turn left by 45 degrees to position for next petal (360/8)

# Draw center of flower
flower.penup()                  # Lift the pen to move without drawing
flower.goto(0, -20)             # Move to the center bottom of the flower to draw the circle
flower.pendown()                # Put the pen down to start drawing
flower.color("yellow")          # Change color to yellow for the center
flower.begin_fill()             # Start filling the shape with yellow
flower.circle(20)               # Draw a filled circle with radius 20
flower.end_fill()               # End filling

# Hide turtle and finish
flower.hideturtle()             # Hide the turtle cursor from the screen
screen.mainloop()               # Keep the window open until manually closed