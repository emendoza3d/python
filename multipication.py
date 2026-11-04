# Multiplication Table Quiz
# Touch-friendly Kivy GUI for Android and desktop

import random

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput


class MultiplicationQuiz(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=12, **kwargs)

        Window.clearcolor = (0.956, 0.972, 1, 1)

        self.score = 0
        self.question_number = 1
        self.pending_event = None

        self.question_label = Label(
            text="",
            font_size="28sp",
            color=(0.12, 0.16, 0.27, 1),
            size_hint_y=None,
            height=70,
        )
        self.add_widget(self.question_label)

        self.answer_entry = TextInput(
            font_size="24sp",
            multiline=False,
            input_filter="int",
            halign="center",
            size_hint=(None, None),
            size=(140, 48),
            pos_hint={"center_x": 0.5},
        )
        self.answer_entry.bind(on_text_validate=self.check_answer)
        self.add_widget(self.answer_entry)

        self.submit_button = Button(
            text="Check Answer",
            font_size="18sp",
            size_hint=(0.75, None),
            height=52,
            pos_hint={"center_x": 0.5},
            background_color=(0.357, 0.553, 0.937, 1),
        )
        self.submit_button.bind(on_press=self.check_answer)
        self.add_widget(self.submit_button)

        self.status_label = Label(
            text="",
            font_size="18sp",
            color=(0.15, 0.27, 0.32, 1),
            size_hint_y=None,
            height=50,
        )
        self.add_widget(self.status_label)

        self.next_question()

    def next_question(self, _dt=None):
        self.pending_event = None
        if self.question_number > 10:
            self.show_final_score()
            return

        self.answer_entry.text = ""
        self.answer_entry.disabled = False
        self.submit_button.disabled = False
        self.answer_entry.focus = True

        self.num1 = random.randint(1, 12)
        self.num2 = random.randint(1, 12)
        self.correct_answer = self.num1 * self.num2

        self.question_label.text = f"{self.num1} x {self.num2} = ?"
        self.status_label.text = f"Question {self.question_number} of 10"

    def check_answer(self, _instance=None):
        if self.pending_event is not None:
            return

        try:
            user_answer = int(self.answer_entry.text)
        except (TypeError, ValueError):
            self.status_label.text = "Please type a number."
            self.answer_entry.text = ""
            return

        if user_answer == self.correct_answer:
            self.score += 1
            self.status_label.text = "Correct! Great job!"
        else:
            self.status_label.text = f"Not quite. The answer is {self.correct_answer}."

        self.question_number += 1
        self.answer_entry.text = ""
        self.answer_entry.disabled = True
        self.submit_button.disabled = True

        delay = 1.5 if self.question_number > 10 else 1.2
        self.pending_event = Clock.schedule_once(
            self.show_final_score if self.question_number > 10 else self.next_question,
            delay,
        )

    def show_final_score(self, _dt=None):
        self.pending_event = None
        self.answer_entry.disabled = True
        self.submit_button.disabled = True

        message = f"You scored {self.score} out of 10!"
        if self.score == 10:
            message += "\nAmazing work!"
        elif self.score >= 7:
            message += "\nGreat job!"
        elif self.score >= 4:
            message += "\nNice effort!"
        else:
            message += "\nKeep practicing!"

        result_label = Label(
            text=message,
            halign="center",
            valign="middle",
            font_size="20sp",
        )
        result_label.bind(size=lambda instance, _size: setattr(instance, "text_size", instance.size))

        close_button = Button(text="Close", size_hint_y=None, height=48)
        play_again_button = Button(text="Play Again", size_hint_y=None, height=48)
        popup = Popup(
            title="Quiz Complete",
            content=BoxLayout(orientation="vertical", padding=10, spacing=10),
            size_hint=(0.85, 0.55),
        )
        popup.content.add_widget(result_label)
        popup.content.add_widget(close_button)
        popup.content.add_widget(play_again_button)

        close_button.bind(on_press=lambda _instance: self.stop_app(popup))
        play_again_button.bind(on_press=lambda _instance: self.restart_game(popup))
        popup.open()

    def stop_app(self, popup):
        popup.dismiss()
        App.get_running_app().stop()

    def restart_game(self, popup):
        popup.dismiss()
        self.score = 0
        self.question_number = 1
        Clock.schedule_once(self.next_question, 0)


class MultiplicationQuizApp(App):
    def build(self):
        return MultiplicationQuiz()


if __name__ == "__main__":
    MultiplicationQuizApp().run()
