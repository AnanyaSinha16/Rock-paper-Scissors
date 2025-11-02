import random
import tkinter as tk
from tkinter import messagebox

CHOICES = ["Rock", "Paper", "Scissors"]

def decide_winner(player, comp):
    if player == comp:
        return "Tie"
    wins = {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper"
    }
    return "You win!" if wins[player] == comp else "You lose!"

class RPSApp:
    def __init__(self, root):  # ✅ Fixed __init__
        self.root = root
        root.title("Rock Paper Scissors")
        root.resizable(False, False)
        self.score_player = 0
        self.score_comp = 0

        # Heading
        tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 16, "bold")).pack(pady=8)

        # Score
        self.score_label = tk.Label(root, text=self._score_text(), font=("Helvetica", 12))
        self.score_label.pack(pady=4)

        # Result display
        self.result_var = tk.StringVar(value="Make your move!")
        tk.Label(root, textvariable=self.result_var, font=("Helvetica", 12)).pack(pady=6)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=6, padx=6)
        for choice in CHOICES:
            b = tk.Button(btn_frame, text=choice, width=10,
                          command=lambda c=choice: self.play(c))
            b.pack(side="left", padx=6)

        # Reset & Quit
        bottom = tk.Frame(root)
        bottom.pack(pady=8)
        tk.Button(bottom, text="Reset Score", command=self.reset_score).pack(side="left", padx=6)
        tk.Button(bottom, text="Quit", command=root.quit).pack(side="left", padx=6)

    def _score_text(self):
        return f"You: {self.score_player} — Computer: {self.score_comp}"

    def play(self, player_choice):
        comp_choice = random.choice(CHOICES)
        result = decide_winner(player_choice, comp_choice)

        if result == "You win!":
            self.score_player += 1
        elif result == "You lose!":
            self.score_comp += 1

        self.score_label.config(text=self._score_text())
        self.result_var.set(f"You: {player_choice}  —  Computer: {comp_choice}\n{result}")

    def reset_score(self):
        if messagebox.askyesno("Reset Score", "Reset both scores to zero?"):
            self.score_player = 0
            self.score_comp = 0
            self.score_label.config(text=self._score_text())
            self.result_var.set("Make your move!")

# ✅ Fixed __name__ check
if __name__ == "__main__":
    root = tk.Tk()
    app = RPSApp(root)
    root.mainloop()
