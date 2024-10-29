from tkinter import *
import random


def restart():
    global player
    # Reset player and update the turn label
    player = random.choice(characters)
    label.config(text=player + "'s turn")

    # Clear all button text
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", state=NORMAL)


def next_turn(row, column):
    global player

    # Only proceed if the button is empty and there's no winner
    if buttons[row][column]['text'] == "" and check_winner() is False:
        buttons[row][column].config(text=player)

        # Check for a winner or tie after the player's move
        result = check_winner()
        if result == True:
            label.config(text=(player + " won!"))
            disable_buttons()
        elif result == "Tie":
            label.config(text="It's a Tie!")
        else:
            # Switch players
            player = characters[1] if player == characters[0] else characters[0]
            label.config(text=(player + "'s turn"))


def check_winner():
    # Check rows and columns for a winner
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != '':
            return True
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != '':
            return True

    # Check diagonals for a winner
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        return True

    # Check for a tie if all spaces are filled
    if empty_spaces() is False:
        return "Tie"
    return False


def empty_spaces():
    # Check if any button is still empty
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == '':
                return True
    return False


def disable_buttons():
    # Disable all buttons once the game is over
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(state=DISABLED)


# Initialize the main game window
board = Tk()
board.title("Tic-Tac-Toe")

characters = ["X", "O"]
player = random.choice(characters)

buttons = [['', '', ''],
           ['', '', ''],
           ['', '', '']]

# Label to display the current player's turn
label = Label(text=player + "'s turn", font=("Futura", 24))
label.pack(side="top")

# Button to start a new game
new_game_button = Button(text="New Game", font=("Futura", 16), command=restart)
new_game_button.pack(side="top")

# Frame for the Tic-Tac-Toe grid
frame = Frame(board)
frame.pack()

# Create the 3x3 grid of buttons
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('Consolas', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

board.mainloop()