import turtle  # Import the turtle graphics module for drawing

# --- Set up the screen ---
screen = turtle.Screen()  # Create a screen object to display the drawing
screen.bgcolor("white")  # Set the background color of the screen to white
screen.title("8-Petal Flower with Stem, Leaf, and Pot")  # Set the window title to describe the drawing

# --- Create the turtle ---
flower = turtle.Turtle()  # Create a turtle named 'flower' to draw the flower
flower.shape("turtle")  # Set the turtle shape to look like a turtle
flower.pensize(2)  # Set the pen size (thickness of lines) to 2
flower.speed(6)  # Set turtle speed (6 is medium-fast)

# --- Create the text turtle ---
text_turtle = turtle.Turtle()  # Create another turtle just for writing text
text_turtle.hideturtle()  # Hide the turtle cursor for neatness
text_turtle.penup()  # Lift pen so it doesn't draw lines while moving
text_turtle.goto(0, 180)  # Move to position above the flower
text_turtle.write("🌻 My Beautiful Flower 🌼", align="center", font=("Times New Roman", 20, "bold"))  # Write decorative text

# --- Draw Petals ---
flower.color("red", "light yellow")  # Set pen color to red and fill color to light yellow

# Define a function to draw one petal using two arcs
def draw_petal():
    flower.begin_fill()  # Start filling the shape
    for _ in range(2):  # Repeat twice to form a petal using arcs
        flower.circle(100, 60)  # Draw an arc with radius 100 and 60 degrees
        flower.left(120)  # Turn left to position for next arc
    flower.end_fill()  # Finish filling the petal

# Draw 8 petals arranged in a circle
for _ in range(8):
    draw_petal()  # Draw a single petal
    flower.left(45)  # Rotate left by 45° to place the next petal evenly (360° / 8)

# --- Draw Flower Center ---
flower.penup()  # Lift pen to move without drawing
flower.goto(0, -20)  # Move to the center of the flower
flower.pendown()  # Put the pen down to start drawing
flower.color("orange")  # Set fill color for flower center
flower.begin_fill()  # Begin filling the circle
flower.circle(20)  # Draw the central circle of the flower
flower.end_fill()  # End the fill

# --- Draw Stem ---
flower.penup()  # Lift pen to move
flower.goto(6, -40)  # Move to just below the flower
flower.setheading(-90)  # Set turtle to face downward
flower.color("green")  # Set pen color to green for stem
flower.pendown()  # Put pen down to draw
flower.pensize(4)  # Thicker line for the stem
flower.forward(150)  # Draw stem downwards

# --- Define Leaf Drawing Function ---
def draw_leaf():
    flower.begin_fill()  # Start filling the leaf
    flower.circle(40, 60)  # First arc (half leaf)
    flower.color("light green")  # Change color for second arc
    flower.left(120)  # Turn left for second half of leaf
    flower.circle(40, 60)  # Second arc
    flower.color("darkgreen")  # Restore color
    flower.end_fill()  # Finish the leaf

# --- Draw Leaf 1 (Left Side) ---
flower.penup()  # Lift pen to reposition
flower.backward(100)  # Move upward on the stem
flower.left(10)  # Slight angle for natural look
flower.forward(20)  # Offset slightly from stem
flower.setheading(-60)  # Face direction to draw leaf on left
flower.color("darkgreen")  # Set color for leaf
flower.pendown()  # Start drawing
draw_leaf()  # Call leaf drawing function

# --- Draw Leaf 2 (Right Side, Lower) ---
flower.penup()  # Lift pen
flower.goto(6, -180)  # Move lower down the stem
flower.right(80)  # Slight angle to the right
flower.forward(20)  # Offset from the stem
flower.setheading(120)  # Face to draw right-side leaf
flower.color("darkgreen")  # Leaf color
flower.pendown()  # Start drawing
draw_leaf()  # Draw the second leaf

# --- Draw Flower Pot ---
flower.penup()  # Lift pen
flower.goto(-15, -193)  # Move to position for pot
flower.setheading(0)  # Face right
flower.color("saddlebrown")  # Set pot color
flower.pensize(2)  # Set pen size
flower.pendown()  # Start drawing
flower.begin_fill()  # Begin filling the pot shape

flower.forward(80)  # Top edge of pot
flower.right(100)  # Turn to draw side
flower.forward(50)  # Right side
flower.right(80)  # Turn to draw bottom
flower.forward(100)  # Bottom edge
flower.right(80)  # Turn to draw left side
flower.forward(50)  # Left side
flower.right(100)  # Back to original orientation
flower.end_fill()  # Finish pot fill

# --- Finish ---
flower.hideturtle()  # Hide the turtle after drawing
screen.mainloop()  # Keep the window open until closed manually