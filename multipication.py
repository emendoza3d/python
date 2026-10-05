# Multiplication Table Quiz
# Simple GUI version for young learners

import random
import tkinter as tk
from tkinter import messagebox


class MultiplicationQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Multiplication Quiz")
        self.root.geometry("450x260")
        self.root.config(bg="#f4f8ff")

        self.score = 0
        self.question_number = 1

        self.question_label = tk.Label(
            root,
            text="",
            font=("Arial", 24, "bold"),
            bg="#f4f8ff",
            fg="#1f2a44",
        )
        self.question_label.pack(pady=(20, 10))

        self.answer_entry = tk.Entry(root, font=("Arial", 18), width=8)
        self.answer_entry.pack(pady=10)
        self.answer_entry.bind("<Return>", self.check_answer)

        self.submit_button = tk.Button(
            root,
            text="Check Answer",
            font=("Arial", 14, "bold"),
            bg="#5b8def",
            fg="white",
            command=self.check_answer,
        )
        self.submit_button.pack(pady=5)

        self.status_label = tk.Label(
            root,
            text="",
            font=("Arial", 14),
            bg="#f4f8ff",
            fg="#264653",
        )
        self.status_label.pack(pady=8)

        self.next_question()

    def next_question(self):
        if self.question_number > 10:
            self.show_final_score()
            return

        self.answer_entry.delete(0, tk.END)
        self.answer_entry.focus()

        self.num1 = random.randint(1, 12)
        self.num2 = random.randint(1, 12)
        self.correct_answer = self.num1 * self.num2

        self.question_label.config(text=f"{self.num1} x {self.num2} = ?")
        self.status_label.config(text=f"Question {self.question_number} of 10")

    def check_answer(self, event=None):
        try:
            user_answer = int(self.answer_entry.get())
        except ValueError:
            self.status_label.config(text="Please type a number.")
            self.answer_entry.delete(0, tk.END)
            return

        if user_answer == self.correct_answer:
            self.score += 1
            self.status_label.config(text="Correct! Great job! 🎉")
        else:
            self.status_label.config(
                text=f"Not quite. The answer is {self.correct_answer}."
            )

        self.question_number += 1
        self.answer_entry.delete(0, tk.END)

        if self.question_number <= 10:
            self.root.after(1200, self.next_question)
        else:
            self.root.after(1500, self.show_final_score)

    def show_final_score(self):
        self.answer_entry.config(state="disabled")
        self.submit_button.config(state="disabled")

        message = f"You scored {self.score} out of 10!"

        if self.score == 10:
            message += "\nAmazing work!"
        elif self.score >= 7:
            message += "\nGreat job!"
        elif self.score >= 4:
            message += "\nNice effort!"
        else:
            message += "\nKeep practicing!"

        self.question_label.config(text=message)
        self.status_label.config(text="Click the X to close this game.")

        play_again = messagebox.askyesno("Play Again?", "Would you like to play again?")
        if play_again:
            self.restart_game()
        else:
            self.root.destroy()

    def restart_game(self):
        self.score = 0
        self.question_number = 1
        self.answer_entry.config(state="normal")
        self.submit_button.config(state="normal")
        self.next_question()


root = tk.Tk()
app = MultiplicationQuiz(root)
root.mainloop()
