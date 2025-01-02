import tkinter as tk  # GUI library for creating the game window
import random  # Library to generate random positions for the food

# Define the Snake class
class Snake:
    def __init__(self):
        """
        Initialize the Snake object with a default body position and graphical representation.
        """
        self.body = [[250, 250], [240, 250], [230, 250]]  # Initial snake body as a list of coordinates
        self.squares = []  # Stores rectangle objects representing snake body parts
        for x, y in self.body:
            self.squares.append(canvas.create_rectangle(x, y, x + 10, y + 10, fill='green'))

    def move(self, direction):
        """
        Move the snake in the specified direction by updating its head position.

        Args:
            direction (str): The current direction of movement ('Up', 'Down', 'Left', 'Right').
        """
        head_x, head_y = self.body[0]  # Get the current head position
        # Determine new head position based on direction
        if direction == 'Up':
            new_head = [head_x, head_y - 10]
        elif direction == 'Down':
            new_head = [head_x, head_y + 10]
        elif direction == 'Left':
            new_head = [head_x - 10, head_y]
        elif direction == 'Right':
            new_head = [head_x + 10, head_y]
        self.body.insert(0, new_head)  # Add the new head position to the body
        self.squares.insert(0, canvas.create_rectangle(new_head[0], new_head[1], new_head[0] + 10, new_head[1] + 10, fill='green'))

    def delete_last(self):
        """
        Remove the last segment of the snake (used to simulate movement).
        """
        self.body.pop()  # Remove the last coordinate from the body
        canvas.delete(self.squares.pop())  # Delete the last rectangle from the canvas

# Define the Food class
class Food:
    def __init__(self):
        """
        Initialize the Food object by placing it at a random location on the grid.
        """
        self.x = random.randint(0, 49) * 10  # Random x-coordinate on a 500x500 grid
        self.y = random.randint(0, 49) * 10  # Random y-coordinate on a 500x500 grid
        self.square = canvas.create_rectangle(self.x, self.y, self.x + 10, self.y + 10, fill='red')

def next_turn():
    """
    Handle the game logic for each frame, including snake movement, collision detection, and scoring.
    """
    global direction
    snake.move(direction)  # Move the snake
    head_x, head_y = snake.body[0]  # Get the snake's head position
    
    # Check for collisions with the wall or itself
    if head_x < 0 or head_x > 490 or head_y < 0 or head_y > 490:
        game_over()
    elif head_x == food.x and head_y == food.y:
        # Snake eats food: increase score and generate new food
        score_label.config(text='Score: ' + str(int(score_label.cget('text').split(': ')[1]) + 1))
        canvas.delete(food.square)  # Remove the current food
        food.__init__()  # Reinitialize food at a new location
    else:
        # If no food is eaten, remove the last segment of the snake
        snake.delete_last()
    
    # Schedule the next frame if the game is not over
    if not game_over_flag:
        window.after(100, next_turn)

def change_direction(event):
    """
    Change the direction of the snake based on user input.

    Args:
        event (tk.Event): Key press event containing the direction key.
    """
    global direction
    # Prevent the snake from reversing direction
    if event.keysym == 'Up' and direction != 'Down':
        direction = 'Up'
    elif event.keysym == 'Down' and direction != 'Up':
        direction = 'Down'
    elif event.keysym == 'Left' and direction != 'Right':
        direction = 'Left'
    elif event.keysym == 'Right' and direction != 'Left':
        direction = 'Right'

def game_over():
    """
    End the game and display the 'Game Over' message.
    """
    global game_over_flag
    game_over_flag = True  # Set game over flag to true
    canvas.delete('all')  # Clear the canvas
    canvas.create_text(250, 250, text='Game Over', font=('Arial', 24), fill='red')  # Display Game Over message

# Initialize the game window
window = tk.Tk()
window.title('Snake Game')  # Set the window title
window.resizable(False, False)  # Disable window resizing

# Create a canvas for the game board
canvas = tk.Canvas(window, width=500, height=500, bg='black')
canvas.pack()

# Create a score label
score_label = tk.Label(window, text='Score: 0', font=('Arial', 24))
score_label.pack()

# Initialize game variables
direction = 'Right'  # Initial direction of the snake
game_over_flag = False  # Flag to check if the game is over
snake = Snake()  # Create a Snake object
food = Food()  # Create a Food object

# Bind keyboard inputs to control the snake
window.bind('<Key>', change_direction)

# Start the game loop
next_turn()

# Run the main loop for the Tkinter window
window.mainloop()
