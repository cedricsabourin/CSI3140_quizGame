import tkinter as tk
from tkinter import messagebox
import random

from questions import questions


# Normal mode colors
NORMAL_BACKGROUND = "#EAF6F6"
NORMAL_CARD = "#FFFFFF"
NORMAL_BUTTON = "#A7D7C5"
NORMAL_BUTTON_HOVER = "#8FCFB5"
NORMAL_TEXT = "#243B3B"

# Boss mode colors
BOSS_BACKGROUND = "#1E1E2E"
BOSS_CARD = "#2A2A40"
BOSS_BUTTON = "#FFB86C"
BOSS_BUTTON_HOVER = "#FF9F43"
BOSS_TEXT = "#F8F8F2"

CORRECT_COLOR = "#2E7D32"
INCORRECT_COLOR = "#C62828"


class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Boss Quiz Game")

        # Responsive window setup
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        start_width = int(screen_width * 0.90)
        start_height = int(screen_height * 0.88)

        self.root.geometry(f"{start_width}x{start_height}")
        self.root.minsize(850, 650)
        self.root.resizable(True, True)

        # On Windows, this opens the app maximized.
        # If it fails on another system, the normal responsive size still works.
        try:
            self.root.state("zoomed")
        except tk.TclError:
            pass

        self.current_question = 0
        self.score = 0
        self.streak = 0
        self.boss_mode = False
        self.answer_submitted = False

        self.selected_answer = tk.StringVar(value="NONE")

        self.quiz_questions = questions.copy()
        random.shuffle(self.quiz_questions)

        self.background_color = NORMAL_BACKGROUND
        self.card_color = NORMAL_CARD
        self.button_color = NORMAL_BUTTON
        self.button_hover_color = NORMAL_BUTTON_HOVER
        self.text_color = NORMAL_TEXT

        self.root.configure(bg=self.background_color)

        # Scrollable layout
        self.canvas = tk.Canvas(
            self.root,
            bg=self.background_color,
            highlightthickness=0
        )
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(
            self.root,
            orient="vertical",
            command=self.canvas.yview
        )
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.outer_frame = tk.Frame(self.canvas, bg=self.background_color)

        self.canvas_window = self.canvas.create_window(
            (0, 0),
            window=self.outer_frame,
            anchor="n"
        )

        self.outer_frame.bind(
            "<Configure>",
            lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.bind("<Configure>", self.resize_content)

        # Mouse wheel scrolling
        self.root.bind_all("<MouseWheel>", self.on_mousewheel)

        self.card = tk.Frame(
            self.outer_frame,
            bg=self.card_color,
            padx=35,
            pady=25
        )
        self.card.pack(padx=40, pady=30, fill="both", expand=True)

        self.top_bar = tk.Frame(self.card, bg=self.card_color)
        self.top_bar.pack(fill="x")

        self.title_label = tk.Label(
            self.top_bar,
            text="Quiz Game",
            font=("Arial", 30, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )
        self.title_label.pack(side="left")

        self.boss_button = tk.Button(
            self.top_bar,
            text="Activate Boss Mode",
            font=("Arial", 12, "bold"),
            bg=self.button_color,
            fg=self.text_color,
            activebackground=self.button_hover_color,
            activeforeground=self.text_color,
            relief="flat",
            padx=16,
            pady=7,
            command=self.toggle_boss_mode
        )
        self.boss_button.pack(side="right")

        self.stats_frame = tk.Frame(self.card, bg=self.card_color)
        self.stats_frame.pack(fill="x", pady=12)

        self.score_label = tk.Label(
            self.stats_frame,
            text="Score: 0",
            font=("Arial", 14, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )
        self.score_label.pack(side="left", padx=10)

        self.streak_label = tk.Label(
            self.stats_frame,
            text="Streak: 0",
            font=("Arial", 14, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )
        self.streak_label.pack(side="left", padx=25)

        self.counter_label = tk.Label(
            self.stats_frame,
            text="",
            font=("Arial", 14, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )
        self.counter_label.pack(side="right", padx=10)

        self.progress_canvas = tk.Canvas(
            self.card,
            height=24,
            bg="#DDEEEE",
            highlightthickness=0
        )
        self.progress_canvas.pack(fill="x", pady=8)

        self.question_label = tk.Label(
            self.card,
            text="",
            font=("Arial", 17, "bold"),
            justify="center",
            bg=self.card_color,
            fg=self.text_color
        )
        self.question_label.pack(fill="x", pady=18)

        self.options_frame = tk.Frame(self.card, bg=self.card_color)
        self.options_frame.pack(fill="x", pady=5)

        self.option_buttons = []

        for i in range(4):
            button = tk.Radiobutton(
                self.options_frame,
                text="",
                variable=self.selected_answer,
                value="",
                font=("Arial", 14),
                anchor="w",
                justify="left",
                bg=self.card_color,
                fg=self.text_color,
                activebackground=self.card_color,
                activeforeground=self.text_color,
                selectcolor=self.background_color,
                padx=10,
                pady=5
            )
            button.pack(fill="x", padx=40, pady=5)
            self.option_buttons.append(button)

        self.feedback_label = tk.Label(
            self.card,
            text="Choose an answer, then press Submit.",
            font=("Arial", 13, "bold"),
            justify="center",
            bg=self.card_color,
            fg=self.text_color
        )
        self.feedback_label.pack(fill="x", pady=10)

        self.reason_label = tk.Label(
            self.card,
            text="",
            font=("Arial", 12),
            justify="center",
            bg=self.card_color,
            fg=self.text_color
        )
        self.reason_label.pack(fill="x", pady=5)

        self.button_frame = tk.Frame(self.card, bg=self.card_color)
        self.button_frame.pack(pady=15)

        self.submit_button = tk.Button(
            self.button_frame,
            text="Submit Answer",
            font=("Arial", 14, "bold"),
            bg=self.button_color,
            fg=self.text_color,
            activebackground=self.button_hover_color,
            activeforeground=self.text_color,
            relief="flat",
            padx=28,
            pady=10,
            command=self.check_answer
        )
        self.submit_button.grid(row=0, column=0, padx=12, pady=5)

        self.next_button = tk.Button(
            self.button_frame,
            text="Next Question",
            font=("Arial", 14, "bold"),
            bg=self.button_color,
            fg=self.text_color,
            activebackground=self.button_hover_color,
            activeforeground=self.text_color,
            relief="flat",
            padx=28,
            pady=10,
            command=self.next_question,
            state="disabled"
        )
        self.next_button.grid(row=0, column=1, padx=12, pady=5)

        self.restart_button = tk.Button(
            self.button_frame,
            text="Restart Quiz",
            font=("Arial", 14, "bold"),
            bg=self.button_color,
            fg=self.text_color,
            activebackground=self.button_hover_color,
            activeforeground=self.text_color,
            relief="flat",
            padx=28,
            pady=10,
            command=self.restart_quiz
        )
        self.restart_button.grid(row=0, column=2, padx=12, pady=5)

        self.load_question()

    def resize_content(self, event):
        canvas_width = event.width

        # Outer frame fills the current screen/window width
        self.canvas.itemconfig(self.canvas_window, width=canvas_width)

        # Responsive wrap sizes
        wrap_width = max(600, canvas_width - 220)

        self.question_label.config(wraplength=wrap_width)
        self.feedback_label.config(wraplength=wrap_width)
        self.reason_label.config(wraplength=wrap_width)

        for button in self.option_buttons:
            button.config(wraplength=wrap_width - 80)

        self.update_progress_bar()

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def toggle_boss_mode(self):
        self.boss_mode = not self.boss_mode

        if self.boss_mode:
            self.background_color = BOSS_BACKGROUND
            self.card_color = BOSS_CARD
            self.button_color = BOSS_BUTTON
            self.button_hover_color = BOSS_BUTTON_HOVER
            self.text_color = BOSS_TEXT
            self.title_label.config(text="BOSS MODE QUIZ")
            self.boss_button.config(text="Deactivate Boss Mode")
        else:
            self.background_color = NORMAL_BACKGROUND
            self.card_color = NORMAL_CARD
            self.button_color = NORMAL_BUTTON
            self.button_hover_color = NORMAL_BUTTON_HOVER
            self.text_color = NORMAL_TEXT
            self.title_label.config(text="Quiz Game")
            self.boss_button.config(text="Activate Boss Mode")

        self.apply_theme()

    def apply_theme(self):
        self.root.configure(bg=self.background_color)
        self.canvas.configure(bg=self.background_color)
        self.outer_frame.configure(bg=self.background_color)
        self.card.configure(bg=self.card_color)
        self.top_bar.configure(bg=self.card_color)
        self.stats_frame.configure(bg=self.card_color)
        self.options_frame.configure(bg=self.card_color)
        self.button_frame.configure(bg=self.card_color)

        labels = [
            self.title_label,
            self.score_label,
            self.streak_label,
            self.counter_label,
            self.question_label,
            self.feedback_label,
            self.reason_label
        ]

        for label in labels:
            label.configure(bg=self.card_color, fg=self.text_color)

        buttons = [
            self.submit_button,
            self.next_button,
            self.restart_button,
            self.boss_button
        ]

        for button in buttons:
            button.configure(
                bg=self.button_color,
                fg=self.text_color,
                activebackground=self.button_hover_color,
                activeforeground=self.text_color
            )

        for button in self.option_buttons:
            button.configure(
                bg=self.card_color,
                fg=self.text_color,
                activebackground=self.card_color,
                activeforeground=self.text_color,
                selectcolor=self.background_color
            )

        self.update_progress_bar()

    def update_progress_bar(self):
        self.progress_canvas.delete("all")

        total_questions = len(self.quiz_questions)
        progress = (self.current_question + 1) / total_questions

        canvas_width = self.progress_canvas.winfo_width()

        if canvas_width <= 1:
            canvas_width = 1000

        bar_width = int(canvas_width * progress)

        if self.boss_mode:
            background = "#44445A"
            fill = "#FFB86C"
        else:
            background = "#DDEEEE"
            fill = "#8FCFB5"

        self.progress_canvas.configure(bg=background)

        self.progress_canvas.create_rectangle(
            0,
            0,
            bar_width,
            24,
            fill=fill,
            outline=""
        )

        self.progress_canvas.create_text(
            canvas_width // 2,
            12,
            text=f"{round(progress * 100)}%",
            fill=self.text_color,
            font=("Arial", 11, "bold")
        )

    def load_question(self):
        self.canvas.yview_moveto(0)

        self.answer_submitted = False
        self.selected_answer.set("NONE")

        self.feedback_label.config(
            text="Choose an answer, then press Submit.",
            fg=self.text_color
        )
        self.reason_label.config(text="", fg=self.text_color)

        self.submit_button.config(state="normal")
        self.next_button.config(state="disabled")

        question_data = self.quiz_questions[self.current_question]

        self.counter_label.config(
            text=f"Question {self.current_question + 1} of {len(self.quiz_questions)}"
        )

        self.question_label.config(text=question_data["question"])

        for i, option in enumerate(question_data["options"]):
            option_letter = option[0]

            self.option_buttons[i].config(
                text=option,
                value=option_letter,
                state="normal",
                bg=self.card_color,
                fg=self.text_color,
                activebackground=self.card_color,
                activeforeground=self.text_color,
                selectcolor=self.background_color
            )

        self.update_progress_bar()

    def check_answer(self):
        if self.answer_submitted:
            return

        user_answer = self.selected_answer.get()

        if user_answer == "NONE":
            messagebox.showwarning(
                "No Answer Selected",
                "Please select an answer before submitting."
            )
            return

        self.answer_submitted = True

        question_data = self.quiz_questions[self.current_question]
        correct_answer = question_data["answer"]

        selected_text = self.get_option_text(user_answer)
        correct_text = self.get_option_text(correct_answer)

        if user_answer == correct_answer:
            self.score += 1
            self.streak += 1

            self.feedback_label.config(
                text=f"Correct! Streak increased to {self.streak}.",
                fg=CORRECT_COLOR
            )

            self.reason_label.config(
                text=f"Reason: {question_data['reason']}",
                fg=CORRECT_COLOR
            )
        else:
            self.streak = 0

            self.feedback_label.config(
                text="Incorrect.",
                fg=INCORRECT_COLOR
            )

            self.reason_label.config(
                text=(
                    f"Your answer: {selected_text}\n\n"
                    f"Correct answer: {correct_text}\n\n"
                    f"Reason: {question_data['reason']}"
                ),
                fg=INCORRECT_COLOR
            )

        self.score_label.config(text=f"Score: {self.score}")
        self.streak_label.config(text=f"Streak: {self.streak}")

        self.highlight_answers(user_answer, correct_answer)

        for button in self.option_buttons:
            button.config(state="disabled")

        self.submit_button.config(state="disabled")
        self.next_button.config(state="normal")

    def get_option_text(self, answer_letter):
        question_data = self.quiz_questions[self.current_question]

        for option in question_data["options"]:
            if option.startswith(answer_letter + ")"):
                return option

        return answer_letter

    def highlight_answers(self, user_answer, correct_answer):
        for button in self.option_buttons:
            option_letter = button.cget("value")

            if option_letter == correct_answer:
                button.config(bg="#DFF5E1", fg="#1B5E20")
            elif option_letter == user_answer and user_answer != correct_answer:
                button.config(bg="#FADDDD", fg="#8B0000")
            else:
                button.config(bg=self.card_color, fg=self.text_color)

    def next_question(self):
        if not self.answer_submitted:
            messagebox.showinfo(
                "Submit First",
                "Please submit your answer before moving to the next question."
            )
            return

        self.current_question += 1

        if self.current_question >= len(self.quiz_questions):
            self.end_quiz()
        else:
            self.load_question()

    def restart_quiz(self):
        self.current_question = 0
        self.score = 0
        self.streak = 0
        self.answer_submitted = False

        self.quiz_questions = questions.copy()
        random.shuffle(self.quiz_questions)

        self.score_label.config(text="Score: 0")
        self.streak_label.config(text="Streak: 0")

        self.load_question()

    def end_quiz(self):
        percentage = round((self.score / len(self.quiz_questions)) * 100, 2)

        if percentage >= 90:
            message = "Boss performance. You crushed it."
        elif percentage >= 75:
            message = "Great job. You know this well."
        elif percentage >= 60:
            message = "Good attempt. Review the explanations and try again."
        else:
            message = "Keep practicing. The reasoning explanations will help."

        messagebox.showinfo(
            "Quiz Complete",
            f"You finished the quiz!\n\n"
            f"Final score: {self.score}/{len(self.quiz_questions)}\n"
            f"Percentage: {percentage}%\n\n"
            f"{message}"
        )

        self.restart_quiz()


def main():
    if len(questions) == 0:
        messagebox.showerror(
            "No Questions Found",
            "The questions.py file does not contain any questions."
        )
        return

    root = tk.Tk()
    QuizGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()