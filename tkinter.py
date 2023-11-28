import tkinter as tk
import random

def play_game(player_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    result = determine_winner(player_choice, computer_choice)

    result_label.config(text=f"Computer chose {computer_choice}. {result}")

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Create the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors Game")

# Create buttons for player choices
rock_button = tk.Button(window, text="Rock", command=lambda: play_game("Rock"))
paper_button = tk.Button(window, text="Paper", command=lambda: play_game("Paper"))
scissors_button = tk.Button(window, text="Scissors", command=lambda: play_game("Scissors"))

# Create a label to display the result
result_label = tk.Label(window, text="Choose Rock, Paper, or Scissors")

# Place widgets on the window
rock_button.pack(side=tk.LEFT, padx=10)
paper_button.pack(side=tk.LEFT, padx=10)
scissors_button.pack(side=tk.LEFT, padx=10)
result_label.pack(pady=20)

# Run the Tkinter event loop
window.mainloop()