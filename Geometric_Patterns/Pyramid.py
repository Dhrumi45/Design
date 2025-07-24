import turtle  # Import the turtle graphics module

# Set up the turtle window with specified width and height
turtle.setup(width=700, height=600)

# Reset the turtle (clears screen and resets turtle state)
turtle.reset()

# Hide the turtle cursor (optional for aesthetic reasons)
turtle.hideturtle()

# Set the title of the turtle graphics window
turtle.title("Triangle Spiral Design Pattern")

# Set the turtle speed to maximum (0 is the fastest)
turtle.speed(0)

# Set the background color of the window to black
turtle.bgcolor('black')

# Set color mode to use RGB values from 0.0 to 1.0
turtle.colormode(1.0)

# Initialize counter variables
c = 0      # Used for indexing color list (can include fractional increments)
x = 0      # Distance the turtle moves forward (grows with each step)

# Define a list of RGB colors transitioning smoothly through the spectrum
colors = [
    # red to orange
    (1.00, 0.00, 0.00), (1.00, 0.10, 0.00), (1.00, 0.20, 0.00), (1.00, 0.30, 0.00), (1.00, 0.40, 0.00),
    (1.00, 0.50, 0.00), (1.00, 0.60, 0.00), (1.00, 0.70, 0.00), (1.00, 0.80, 0.00), (1.00, 0.90, 0.00),

    # orange to yellow
    (1.00, 1.00, 0.00), (0.90, 1.00, 0.10), (0.80, 1.00, 0.20), (0.70, 1.00, 0.30), (0.60, 1.00, 0.40),

    # yellow to green
    (0.50, 1.00, 0.50), (0.40, 1.00, 0.60), (0.30, 1.00, 0.70), (0.20, 1.00, 0.80), (0.10, 1.00, 0.90),

    # green shades
    (0.00, 1.00, 0.00), (0.00, 0.90, 0.10), (0.00, 0.80, 0.20), (0.00, 0.70, 0.30), (0.00, 0.60, 0.40),

    # green to blue
    (0.00, 0.50, 0.50), (0.00, 0.40, 0.60), (0.00, 0.30, 0.70), (0.00, 0.20, 0.80), (0.00, 0.10, 0.90),

    # blue shades
    (0.00, 0.00, 1.00), (0.10, 0.00, 1.00), (0.20, 0.00, 1.00), (0.30, 0.00, 1.00), (0.40, 0.00, 1.00),

    # blue to purple
    (0.50, 0.00, 1.00), (0.60, 0.00, 1.00), (0.70, 0.00, 1.00), (0.80, 0.00, 1.00), (0.90, 0.00, 1.00),

    # purple to pink
    (1.00, 0.00, 1.00), (1.00, 0.10, 0.90), (1.00, 0.20, 0.80), (1.00, 0.30, 0.70), (1.00, 0.40, 0.60),

    # pink fading back to red for a smooth loop
    (1.00, 0.50, 0.50), (1.00, 0.60, 0.60), (1.00, 0.70, 0.70), (1.00, 0.80, 0.80), (1.00, 0.90, 0.90)
]

# Store the number of colors for looping
color_count = len(colors)

# Begin drawing triangular spiral pattern
while x < 775:
    idx = int(c) % color_count      # Get color index with wrap-around
    color = colors[idx]             # Fetch current color
    turtle.color(color)             # Set turtle color
    turtle.forward(x)               # Move forward
    turtle.right(120)               # Turn right by 120 degrees for triangle shape
    x += 1                          # Increase step length
    c += 0.1                        # Gradually change color

# Exit on mouse click after drawing
turtle.exitonclick()