# load the packages

from tkinter import *
from chat_3 import get_response_3, bot_name

# set the color for background and text
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOUR = "#EAECEE"

# set the font type
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

# create a class
class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        self.conversation=[]
    
    def run(self):
        a="Rudra: Hey buddy! Welcome to APNA app. I am your personal chatbot. I understand you belong to 40-59 age group. I'm here to help you de-stress and nurture yourself. How can I assist you today?"
        print(a)
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, a)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=700, height=500, bg=BG_COLOR)

        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOUR,
                            text="Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        #tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        #text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOUR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        #bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=50)
        bottom_label.place(relwidth=1, rely=0.825)

        #message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOUR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        #send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
        command= lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
        
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get().lower()

        if msg == 'bye':
            self._insert_message(msg, "You")
            self.conversation.append({"sender":"You","message":msg})
            self.window.after(2000, self.window.destroy)
            return

        self._insert_message(msg, "You")
        self.conversation.append({"sender":"You","message":msg})
        self.save_conversation()

    def _insert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}: {get_response_3(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)
        
    def save_conversation(self):
    # Load existing conversation data
        try:
            with open('conversation.json', 'r') as json_file:
                existing_data = json.load(json_file)
        except FileNotFoundError:
            existing_data = []

    # Append new data to existing data
        existing_data.append(self.conversation)

    # Save the combined data to the JSON file
        with open('conversation.json', 'w') as json_file:
            json.dump(self.conversation, json_file, indent=2)

if __name__ == "__main__":
    app = ChatApplication()
    app.run()