# ------------------------ Importing Libraries ------------------------
import turtle         # Import the turtle graphics module for drawing
import colorsys       # Import colorsys module to convert HSV colors to RGB

# ------------------------ Screen Setup ------------------------

screen = turtle.Screen()             # Create a window screen for turtle graphics
screen.bgcolor("black")              # Set the background color of the screen to black
screen.title("Multiple Rangoli Designs")  # Set the title of the window
turtle.colormode(1.0)                # Set turtle to accept RGB values in range 0.0 - 1.0

# ------------------------ Turtle Setup ------------------------

pen = turtle.Turtle()                # Create a turtle object to draw with
pen.speed(0)                         # Set turtle speed to maximum (no delay)
pen.width(2)                         # Set the width of the pen
pen.hideturtle()                     # Hide the turtle cursor for cleaner output

# ------------------------ Color Palette Generator ------------------------

def generate_colors(n):
    """Generate a list of n bright colors using HSV model."""
    return [colorsys.hsv_to_rgb(i / n, 1.0, 1.0) for i in range(n)]  # Convert HSV to RGB and return n colors

colors = generate_colors(100)        # Generate 100 distinct vibrant colors

# ------------------------ Basic Shapes ------------------------

def draw_polygon(sides, size):
    """Draw a regular polygon with given number of sides and size."""
    angle = 360 / sides              # Calculate the angle between sides
    for _ in range(sides):           # Repeat for each side of the polygon
        pen.forward(size)            # Move pen forward by given size
        pen.right(angle)             # Turn right by calculated angle

def draw_star(size):
    """Draw a 5-point star of given size."""
    for _ in range(5):               # Loop 5 times for 5 star points
        pen.forward(size)            # Move forward by size
        pen.right(144)               # Turn right by 144° to create a star

# ------------------------ Pattern 1: Flower Mandala ------------------------

def rangoli_flower_mandala():
    """Draw a circular flower-like mandala with curved petals."""
    pen.clear()                      # Clear previous drawings

    for i in range(36):              # Draw 36 petals
        pen.penup()                  # Lift pen to reposition
        pen.goto(0, 0)               # Move to center
        pen.setheading(i * 10)       # Rotate heading for next petal
        pen.forward(50)              # Move outward from center
        pen.pendown()                # Start drawing

        pen.color(colors[i % len(colors)])  # Pick a color from the palette
        pen.begin_fill()             # Begin filling the shape with color

        pen.circle(40, 60)           # Draw first arc (curve of petal)
        pen.left(120)                # Turn left to position for second arc
        pen.circle(40, 60)           # Draw second arc (mirror of first)
        pen.end_fill()              # Complete filling

# ------------------------ Pattern 2: Geometric Layers ------------------------

def rangoli_geometric_layers():
    """Draw geometric shapes layered in circular arrangement."""
    pen.clear()                      # Clear the screen
    shapes = [3, 4, 5, 6]            # List of shapes: triangle, square, etc.
    radius = 60                      # Initial radius for first layer
    for idx, sides in enumerate(shapes):  # Loop over each shape
        for i in range(12):         # Repeat 12 times around circle
            angle = 360 / 12        # Angle between repetitions
            pen.penup()
            pen.goto(0, 0)          # Return to center
            pen.setheading(angle * i)  # Set angle for current shape
            pen.forward(radius + idx * 40)  # Move outward depending on layer
            pen.pendown()
            pen.color(colors[(i * 5 + sides) % len(colors)])  # Choose color
            draw_polygon(sides, 40)  # Draw the polygon

# ------------------------ Pattern 3: Starburst ------------------------

def rangoli_starburst():
    """Draw a starburst pattern using 5-point stars."""
    pen.clear()                      # Clear the screen
    for i in range(36):              # 36 repetitions
        pen.penup()
        pen.goto(0, 0)               # Move to center
        pen.setheading(i * 10)       # Rotate for each star
        pen.forward(100)             # Move outward
        pen.pendown()
        pen.color(colors[i % len(colors)])  # Choose color
        draw_star(40)                # Draw a 5-point star

# ------------------------ Pattern 4: Hexagon Grid ------------------------

def rangoli_hex_grid():
    """Draw a grid of hexagons (flower-like)."""
    pen.clear()                      # Clear the screen
    side = 60                        # Length of each hexagon side
    rows = 6                         # Number of rows in grid
    cols = 6                         # Number of columns
    start_x = -180                   # Starting x position
    start_y = 100                    # Starting y position

    for row in range(rows):         # Loop through each row
        for col in range(cols):     # Loop through each column
            x = start_x + col * (side + 10)  # Calculate x coordinate
            y = start_y - row * (side + 10)  # Calculate y coordinate
            pen.penup()
            pen.goto(x, y)          # Move to calculated position
            pen.pendown()
            pen.color(colors[(row * cols + col) % len(colors)])  # Choose color
            draw_polygon(6, side)   # Draw a hexagon

# ------------------------ Pattern 5: Spiral Mandala ------------------------

def rangoli_spiral():
    """Draw a spiral mandala using increasing radius."""
    pen.clear()                      # Clear screen
    for i in range(350):            # Loop to create spiral effect
        pen.color(colors[i % len(colors)])  # Choose color
        pen.forward(i * 0.5)        # Increase distance forward over time
        pen.left(59)                # Slight left turn to create spiral

# ------------------------ Pattern 6: Flower Mandala Circle ------------------------

def rangoli_flower_mandala_circle():
    """Draw a circular flower-like mandala pattern."""
    pen.clear()                      # Clear the screen
    for i in range(36):             # 36 petals
        pen.penup()
        pen.goto(0, 0)              # Go to center
        pen.setheading(i * 10)      # Set angle for current petal
        pen.forward(50)             # Move outward
        pen.pendown()
        pen.color(colors[i % len(colors)])  # Choose color
        pen.begin_fill()
        pen.circle(30)              # Draw a filled circle
        pen.end_fill()

# ------------------------ Interactive Menu ------------------------

def draw_menu():
    """Show pattern selection dialog box using Turtle GUI."""
    menu_text = (
        "🌸 Rangoli Patterns Available:\n"
        "1. Flower Mandala\n"
        "2. Geometric Layers\n"
        "3. Starburst Design\n"
        "4. Hexagon Grid\n"
        "5. Spiral Mandala\n"
        "6. Circle Mandala\n\n"
        "Enter the number of the Rangoli you want to draw:"
    )

    choice = screen.textinput("Choose Rangoli Pattern", menu_text)  # Get user input via dialog

    if choice is None:                # If user clicks cancel or closes input
        turtle.bye()                 # Close turtle window
        return                        # Exit the function

    # Call the corresponding pattern function based on user's choice
    if choice == "1":
        rangoli_flower_mandala()
    elif choice == "2":
        rangoli_geometric_layers()
    elif choice == "3":
        rangoli_starburst()
    elif choice == "4":
        rangoli_hex_grid()
    elif choice == "5":
        rangoli_spiral()
    elif choice == "6":
        rangoli_flower_mandala_circle()
    else:
        # Show error and re-prompt if input is invalid
        screen.textinput("Invalid Choice", "Invalid input. Please enter a number between 1 and 6.")
        draw_menu()

# ------------------------ Start the Program ------------------------

draw_menu()     # Display the pattern selection menu to the user
turtle.done()   # Keep the Turtle window open until it's closed manually
