import tkinter as tk
import random # AI RNG


# Main Menu
root = tk.Tk()
root.title("RPS! Python")
title_frame = tk.Frame(root)
title_frame.pack()

# Logo (
blue_label = tk.Label(
    title_frame, 
    text="RPS!", 
    font=("arial", 12, "italic"), 
    fg="#336E9D"
)
yellow_label = tk.Label(
    title_frame, 
    text=" Python", 
    font=("arial", 12, "bold"), 
    fg="#D1AC36" # darker cuz #FFD643 is too bright for gray/white window backgrounds
)
blue_label.pack(side=tk.LEFT)
yellow_label.pack(side=tk.LEFT)
# )

made_by_label = tk.Label(
    root,
    text="Made by GAB644",
    font=("Arial", 8, "normal")
)
label = tk.Label(root, text="Ready to play?")
made_by_label.pack()
label.pack()
root.geometry("170x120")

# Choose Window
def show_new_window():
    root.withdraw()

    choose_window = tk.Toplevel(root)
    choose_window.title("Choose")
    choose_window.geometry("180x200")

    label = tk.Label(choose_window, text="Rock, Paper, or Scissors?")
    label.pack(pady=10)
    
    # Functions for choices
# rock
    def choose_rock():
        choose_window.destroy()

        result_window = tk.Toplevel(root)
        result_window.title("Chosen Rock")
        result_window.geometry("250x180")

        label = tk.Label(result_window, text="You chose Rock!")
        label.pack(pady=10)

        # AI randomizer
        ai_choices = ["Rock", "Paper", "Scissors"]
        ai_choice = random.choice(ai_choices)
        ai_label = tk.Label(result_window, text=f"AI chose: {ai_choice}")
        ai_label.pack(pady=5)

        # Determine winner
        if ai_choice == "Paper":
            result = "AI Wins!"
            result_color = "red"
        elif ai_choice == "Scissors":
            result = "You Win!"
            result_color = "green"
        else:
            result = "It's a Tie!"
            result_color = "orange"

        result_label = tk.Label(result_window, text=result, fg=result_color, font=("Arial", 12, "bold"))
        result_label.pack(pady=5)
        
        back_button = tk.Button(result_window, text="Back to Menu", 
                               command=lambda: [result_window.destroy(), root.deiconify()])
        back_button.pack()

        result_window.protocol("WM_DELETE_WINDOW", root.destroy)
        
# paper
    def choose_paper():
        choose_window.destroy()

        result_window = tk.Toplevel(root)
        result_window.title("Chosen Paper")
        result_window.geometry("250x200")

        label = tk.Label(result_window, text="You chose Paper!")
        label.pack(pady=10)

        # AI randomizer
        ai_choices = ["Rock", "Paper", "Scissors"]
        ai_choice = random.choice(ai_choices)
        ai_label = tk.Label(result_window, text=f"AI chose: {ai_choice}")
        ai_label.pack(pady=5)

        # Determine winner
        if ai_choice == "Scissors":
            result = "AI Wins!"
            result_color = "red"
        elif ai_choice == "Rock":
            result = "You Win!"
            result_color = "green"
        else:
            result = "It's a Tie!"
            result_color = "orange"

        result_label = tk.Label(result_window, text=result, fg=result_color, font=("Arial", 12, "bold"))
        result_label.pack(pady=5)

        back_button = tk.Button(result_window, text="Back to Menu", 
                               command=lambda: [result_window.destroy(), root.deiconify()])
        back_button.pack()

        result_window.protocol("WM_DELETE_WINDOW", root.destroy)
        
# scissors
    def choose_scissors():
        choose_window.destroy()

        result_window = tk.Toplevel(root)
        result_window.title("Chosen Scissors")
        result_window.geometry("250x200")

        label = tk.Label(result_window, text="You chose Scissors!")
        label.pack(pady=10)

        # AI randomizer
        ai_choices = ["Rock", "Paper", "Scissors"]
        ai_choice = random.choice(ai_choices)
        ai_label = tk.Label(result_window, text=f"AI chose: {ai_choice}")
        ai_label.pack(pady=5)

        # Determine winner
        if ai_choice == "Rock":
            result = "AI Wins!"
            result_color = "red"
        elif ai_choice == "Paper":
            result = "You Win!"
            result_color = "green"
        else:
            result = "It's a Tie!"
            result_color = "orange"

        result_label = tk.Label(result_window, text=result, fg=result_color, font=("Arial", 12, "bold"))
        result_label.pack(pady=5)

        back_button = tk.Button(result_window, text="Back to Menu", 
                               command=lambda: [result_window.destroy(), root.deiconify()])
        back_button.pack()

        result_window.protocol("WM_DELETE_WINDOW", root.destroy)

    # Choice buttons
    rock_button = tk.Button(choose_window, text="Rock", command=choose_rock)
    rock_button.pack(pady=5)

    paper_button = tk.Button(choose_window, text="Paper", command=choose_paper)
    paper_button.pack(pady=5)

    scissors_button = tk.Button(choose_window, text="Scissors", command=choose_scissors)
    scissors_button.pack(pady=5)

    choose_window.protocol("WM_DELETE_WINDOW", root.destroy)

new_window_button = tk.Button(root, text="Play", command=show_new_window)
new_window_button.pack()


exit_button = tk.Button(root, text="Nevermind", 
command=root.destroy)
exit_button.pack()

print("Working!")
root.mainloop()
# Code by GAB644 :]
