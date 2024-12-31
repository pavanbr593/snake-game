import tkinter as tk
import random

class Snake:
    def __init__(self):
        self.body = [[250, 250], [240, 250], [230, 250]]
        self.squares = []
        for x, y in self.body:
            self.squares.append(canvas.create_rectangle(x, y, x + 10, y + 10, fill='green'))

    def move(self, direction):
        head_x, head_y = self.body[0]
        if direction == 'Up':
            new_head = [head_x, head_y - 10]
        elif direction == 'Down':
            new_head = [head_x, head_y + 10]
        elif direction == 'Left':
            new_head = [head_x - 10, head_y]
        elif direction == 'Right':
            new_head = [head_x + 10, head_y]
        self.body.insert(0, new_head)
        self.squares.insert(0, canvas.create_rectangle(new_head[0], new_head[1], new_head[0] + 10, new_head[1] + 10, fill='green'))

    def delete_last(self):
        self.body.pop()
        canvas.delete(self.squares.pop())

class Food:
    def __init__(self):
        self.x = random.randint(0, 49) * 10
        self.y = random.randint(0, 49) * 10
        self.square = canvas.create_rectangle(self.x, self.y, self.x + 10, self.y + 10, fill='red')

def next_turn():
    global direction
    snake.move(direction)
    head_x, head_y = snake.body[0]
    if head_x < 0 or head_x > 490 or head_y < 0 or head_y > 490:
        game_over()
    elif head_x == food.x and head_y == food.y:
        score_label.config(text='Score: ' + str(int(score_label.cget('text').split(': ')[1]) + 1))
        canvas.delete(food.square)
        food.__init__()
    else:
        snake.delete_last()
    
    if not game_over_flag:
        window.after(100, next_turn)

def change_direction(event):
    global direction
    if event.keysym == 'Up' and direction != 'Down':
        direction = 'Up'
    elif event.keysym == 'Down' and direction != 'Up':
        direction = 'Down'
    elif event.keysym == 'Left' and direction != 'Right':
        direction = 'Left'
    elif event.keysym == 'Right' and direction != 'Left':
        direction = 'Right'

def game_over():
    global game_over_flag
    game_over_flag = True
    canvas.delete('all')
    canvas.create_text(250, 250, text='Game Over', font=('Arial', 24), fill='red')

window = tk.Tk()
window.title('Snake Game')
window.resizable(False, False)

canvas = tk.Canvas(window, width=500, height=500, bg='black')
canvas.pack()

score_label = tk.Label(window, text='Score: 0', font=('Arial', 24))
score_label.pack()

direction = 'Right'
game_over_flag = False
snake = Snake()
food = Food()

window.bind('<Key>', change_direction)

next_turn()

window.mainloop()
