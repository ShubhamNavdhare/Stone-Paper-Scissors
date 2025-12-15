import tkinter as tk
import random

# Game logic
def game_win(ai, you):
    if ai == you:
        return None
    elif ai == 'stone':
        return you == 'paper'
    elif ai == 'paper':
        return you == 'scissor'
    elif ai == 'scissor':
        return you == 'stone'

def play(user_choice):
    choices = ['stone', 'paper', 'scissor']
    ai_choice = random.choice(choices)

    result = game_win(ai_choice, user_choice)

    ai_label.config(text=f"Computer chose: {ai_choice.capitalize()}")
    user_label.config(text=f"You chose: {user_choice.capitalize()}")

    if result is None:
        result_label.config(text="Result: It's a Tie 🤝", fg="orange")
    elif result:
        result_label.config(text="Result: You Win 🎉", fg="green")
    else:
        result_label.config(text="Result: You Lose 😢", fg="red")

# UI setup
root = tk.Tk()
root.title("Stone Paper Scissors")
root.geometry("400x350")
root.config(bg="#1e1e2f")

title = tk.Label(root, text="Stone Paper Scissors", font=("Arial", 18, "bold"), bg="#1e1e2f", fg="white")
title.pack(pady=10)

user_label = tk.Label(root, text="", font=("Arial", 12), bg="#1e1e2f", fg="white")
user_label.pack()

ai_label = tk.Label(root, text="", font=("Arial", 12), bg="#1e1e2f", fg="white")
ai_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#1e1e2f")
result_label.pack(pady=15)

button_frame = tk.Frame(root, bg="#1e1e2f")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Stone", width=10, command=lambda: play("stone")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Paper", width=10, command=lambda: play("paper")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Scissor", width=10, command=lambda: play("scissor")).grid(row=0, column=2, padx=5)

root.mainloop()
