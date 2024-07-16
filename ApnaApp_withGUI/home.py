import tkinter as tk
from tkinter import Tk, IntVar, Radiobutton, Label, Entry, Button, StringVar, font, messagebox
import random
import subprocess

class ChatbotApp:
    def __init__(self, master, questions):
        self.master = master
        self.questions = questions
        self.current_question_index = 0
        self.total_points = 0

        # Increase font size
        chat_font = font.Font(size=20)
        self.chat_history = tk.Text(master, wrap="word", width=50, height=15, font=chat_font)
        self.chat_history.pack(side="top", pady=20)

        self.answer_var = StringVar()
        self.answer_entry = tk.Entry(master, textvariable=self.answer_var, width=30, font=chat_font)
        self.answer_entry.pack(side="top", pady=10)

        self.send_button = tk.Button(master, text="Send", command=self.send_answer, font=chat_font)
        self.send_button.pack(side="top", pady=10)

        self.update_chat("Bot: Hi! I'm your friendly chatbot. Let's get started.")

        # Display the first question
        self.display_question()

    def display_question(self):
        question_text = f"Bot: {self.questions[self.current_question_index]['patterns'][0]}\n\n"
        options_text = "\n".join([f"{key}. {value['text']}" for key, value in self.questions[self.current_question_index]['options'].items()])
        self.update_chat(question_text + options_text)

    def send_answer(self):
        user_answer = self.answer_var.get().strip()

        if user_answer:
            self.update_chat(f"User: {user_answer}")
            self.update_chat(f"")

            # Process user's answer
            self.process_answer(user_answer)

            # Clear the answer entry
            self.answer_var.set("")

    def process_answer(self, user_answer):
        selected_option = None

        # Check if the user's answer matches any option
        for option_key, option_value in self.questions[self.current_question_index]["options"].items():
            if user_answer.lower() in option_value["text"].lower():
                selected_option = option_key
                break

        if selected_option:
            points = self.questions[self.current_question_index]["options"][selected_option]["points"]
            self.total_points += points

        # Move to the next question
        self.current_question_index += 1

        if self.current_question_index < len(self.questions):
            # Display the next question
            self.display_question()
        else:
            # Display the result
            self.display_result()

    def display_result(self):
        if self.total_points > 10:
            root.destroy()
            subprocess.run(["python3", "signup.py"])

        else:
            self.update_chat("Bot: You are not valid to use this bot.")
            

        # Disable the answer entry and send button
        self.answer_entry.config(state=tk.DISABLED)
        self.send_button.config(state=tk.DISABLED)

    def update_chat(self, message):
        current_content = self.chat_history.get("1.0", tk.END).strip()
        new_content = f"{current_content}\n{message}\n"
        self.chat_history.config(state=tk.NORMAL)
        self.chat_history.delete("1.0", tk.END)
        self.chat_history.insert(tk.END, new_content)
        self.chat_history.config(state=tk.DISABLED)

        # Automatically scroll to the bottom
        self.chat_history.see(tk.END)

if __name__ == "__main__":
    # Define your questions_data variable here
    questions_data = {
    "intents": [
        {
            "tag": "question1",
            "patterns": [
                "How are you feeling today?"
            ],
            "options": {
                "a": {
                    "text": "Good",
                    "points": 3
                },
                "b": {
                    "text": "Okay",
                    "points": 2
                },
                "c": {
                    "text": "Bad",
                    "points": 1
                }
            }
        },
        {
            "tag": "question2",
            "patterns": [
                "What is your favorite activity?"
            ],
            "options": {
                "a": {
                    "text": "Reading",
                    "points": 2
                },
                "b": {
                    "text": "Exercise",
                    "points": 3
                },
                "c": {
                    "text": "Watching TV",
                    "points": 1
                }
            }
        },
        {
            "tag": "question3",
            "patterns": [
                "How well did you sleep last night?"
            ],
            "options": {
                "a": {
                    "text": "Very well",
                    "points": 3
                },
                "b": {
                    "text": "Average",
                    "points": 2
                },
                "c": {
                    "text": "Poorly",
                    "points": 1
                }
            }
        },
        {
            "tag": "question4",
            "patterns": [
                "What is your preferred relaxation method?"
            ],
            "options": {
                "a": {
                    "text": "Meditation",
                    "points": 3
                },
                "b": {
                    "text": "Listening to music",
                    "points": 2
                },
                "c": {
                    "text": "Taking a walk",
                    "points": 1
                }
            }
        },
        {
            "tag": "question5",
            "patterns": [
                "Do you engage in social activities?"
            ],
            "options": {
                "a": {
                    "text": "Frequently",
                    "points": 3
                },
                "b": {
                    "text": "Occasionally",
                    "points": 2
                },
                "c": {
                    "text": "Rarely",
                    "points": 1
                }
            }
        },
    ]
    }

    root = tk.Tk()
    root.title("Chatbot Questionnaire")

    app = ChatbotApp(root, questions_data["intents"])

    root.mainloop()
