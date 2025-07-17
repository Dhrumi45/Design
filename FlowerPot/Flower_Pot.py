import turtle  # Import the turtle graphics module for drawing

# --- Set up the screen ---
screen = turtle.Screen()  # Create a screen object to serve as the canvas
screen.bgcolor("white")  # Set the background color of the screen to white
screen.title("8-Petal Flower with Stem, Leaf, and Pot")  # Set the title of the window

# --- Create the drawing turtle ---
flower = turtle.Turtle()  # Create a turtle named 'flower' for drawing
flower.shape("turtle")  # Set the turtle cursor shape to a turtle
flower.pensize(3)  # Set the pen thickness to 3
flower.speed(6)  # Set the drawing speed (1 slowest, 10 fastest)

# --- Create the text turtle ---
text_turtle = turtle.Turtle()  # Create a separate turtle for writing text
text_turtle.hideturtle()  # Hide the turtle icon
text_turtle.penup()  # Lift the pen so it doesn't draw when moving
text_turtle.goto(0, 180)  # Move to coordinates above the flower
# Write the text message at the top of the screen
text_turtle.write("Duck You 🦆", align="center", font=("Times New Roman", 20, "bold"))

# --- Draw Petals ---
flower.color("red")  # Set the pen color to red for the petals

# Define a function to draw one petal
def draw_petal():
    for _ in range(2):  # Each petal has 2 arcs
        flower.circle(100, 60)  # Draw an arc with radius 100 and angle 60 degrees
        flower.left(120)  # Turn left to draw the other side of the petal

# Draw 8 petals in a circular pattern
for _ in range(8):
    draw_petal()  # Call the function to draw one petal
    flower.left(45)  # Turn 45 degrees to position the next petal

# --- Draw Flower Center ---
flower.penup()  # Lift pen to reposition without drawing
flower.goto(0, -20)  # Move to the center of the flower
flower.pendown()  # Lower the pen to start drawing
flower.color("orange")  # Set the color for the center of the flower
flower.begin_fill()  # Start filling the shape
flower.circle(20)  # Draw a filled circle as the center
flower.end_fill()  # End the fill

# --- Draw Stem ---
flower.penup()  # Lift pen to move to stem position
flower.goto(6, -40)  # Move slightly below the flower center
flower.setheading(-90)  # Point the turtle downward
flower.color("green")  # Set color to green for the stem
flower.pendown()  # Lower the pen to draw
flower.pensize(4)  # Increase pen size for a thicker stem
flower.forward(150)  # Draw the stem downward

# --- Define Leaf Drawing Function ---
def draw_leaf():
    flower.begin_fill()  # Start filling the leaf shape
    flower.circle(40, 60)  # Draw one arc of the leaf
    flower.left(120)  # Turn to draw the other side
    flower.circle(40, 60)  # Draw the other arc
    flower.end_fill()  # Complete the leaf fill

# --- Draw Leaf 1 ---
flower.penup()  # Lift pen to reposition
flower.backward(100)  # Move up along the stem
flower.left(10)  # Slight left turn to angle the leaf
flower.forward(20)  # Adjust position
flower.setheading(-60)  # Set angle for leaf orientation
flower.color("darkgreen")  # Set leaf color
flower.pendown()  # Lower pen to draw
draw_leaf()  # Call the leaf drawing function

# --- Draw Flower Pot ---
flower.penup()  # Lift pen to reposition
flower.goto(-15, -193)  # Move to pot position at the base
flower.setheading(0)  # Face right to start pot drawing
flower.color("saddlebrown")  # Set color to brown for the pot
flower.pensize(2)  # Set pen size for pot outline
flower.pendown()  # Lower pen to start drawing
flower.begin_fill()  # Begin filling the pot shape

flower.forward(80)  # Draw the top edge of the pot
flower.right(100)  # Turn right for angled side
flower.forward(50)  # Draw right slanted side
flower.right(80)  # Turn for bottom edge
flower.forward(100)  # Draw bottom of the pot
flower.right(80)  # Turn for left slanted side
flower.forward(50)  # Draw left slanted side
flower.right(100)  # Final turn to close the shape
flower.end_fill()  # Complete the pot fill

# --- Finish ---
flower.hideturtle()  # Hide the turtle after drawing is complete
screen.mainloop()  # Keep the window open until the user closes it