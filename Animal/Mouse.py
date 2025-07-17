import turtle  # Imports the turtle graphics library

# === Screen Setup ===
screen = turtle.Screen()  # Creates a screen object
screen.bgcolor("lightgray")  # Sets the background color of the screen
screen.title("Cute Mouse Drawing")  # Sets the window title

# === Turtle Setup ===
mouse = turtle.Turtle()  # Creates a turtle named 'mouse'
mouse.speed(0)  # Sets the turtle's speed to the fastest
mouse.pensize(2)  # Sets the pen thickness
mouse.hideturtle()  # Hides the turtle cursor

# === Function to Draw Filled Circles ===
def draw_circle(x, y, radius, color):
    mouse.penup()  # Lifts the pen to avoid drawing while moving
    mouse.goto(x, y - radius)  # Moves the turtle to the starting point of the circle
    mouse.pendown()  # Puts the pen down to start drawing
    mouse.color(color)  # Sets the drawing color
    mouse.begin_fill()  # Begins filling the shape
    mouse.circle(radius)  # Draws a circle with the given radius
    mouse.end_fill()  # Ends the fill operation

# === Ears ===
draw_circle(-50, 100, 30, "gray")  # Left outer ear
draw_circle(50, 100, 30, "gray")  # Right outer ear
draw_circle(-50, 100, 15, "pink")  # Left inner ear
draw_circle(50, 100, 15, "pink")  # Right inner ear

# === Head ===
draw_circle(0, 60, 60, "gray")  # Head circle

# === Eyes ===
draw_circle(-20, 90, 10, "white")  # Left white eyeball
draw_circle(20, 90, 10, "white")  # Right white eyeball
draw_circle(-20, 90, 4, "black")  # Left black pupil
draw_circle(20, 90, 4, "black")  # Right black pupil

# === Nose ===
draw_circle(0, 60, 5, "black")  # Small black nose

# === Whiskers ===
mouse.color("black")  # Set color to black for whiskers
for y in [60, 55, 65]:  # Loop over three y-coordinates for whiskers
    for direction in [-1, 1]:  # Draw on both left (-1) and right (1) sides
        mouse.penup()  # Lift pen before moving
        mouse.goto(0, y)  # Move to starting whisker position
        mouse.setheading(0)  # Face turtle to the right
        mouse.pendown()  # Start drawing
        mouse.forward(40 * direction)  # Draw whisker line to the left or right

# === Body ===
draw_circle(0, -40, 80, "gray")  # Draws the main body of the mouse

# === Paws ===
draw_circle(-40, -110, 20, "gray")  # Left paw
draw_circle(40, -110, 20, "gray")  # Right paw

# === Tail ===
mouse.penup()  # Lift pen before moving
mouse.goto(60, -120)  # Move to tail starting position
mouse.pendown()  # Start drawing tail
mouse.pensize(3)  # Make the tail thicker
mouse.color("pink")  # Set tail color
mouse.setheading(-45)  # Set angle of tail
for i in range(60):  # Draw a curved tail with a loop
    mouse.forward(2)  # Move forward slightly
    mouse.left(2)  # Slightly curve the tail

# === Text ===
mouse.penup()  # Lift pen before moving
mouse.goto(0, -200)  # Move to position below the drawing
mouse.color("black")  # Set text color
mouse.write("Hi! I'm a Mouse 🐭", align="center", font=("Arial", 16, "bold"))  # Write message

turtle.done()  # Finish turtle drawing and keep the window open