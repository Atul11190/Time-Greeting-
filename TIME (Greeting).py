import time
import tkinter as tk

def greeting():
    current_hour = time.localtime().tm_hour
    if 5 <= current_hour < 12:
        return "Good morning!"
    elif 12 <= current_hour < 17:
        return "Good afternoon!"
    elif 17 <= current_hour < 21:
        return "Good evening!"
    else:
        return "Good night!"

def show_greeting():
    window = tk.Tk()
    window.title("Greeting")
    window.geometry("300x200")
    window.configure(bg="#add8e6")

    greeting_message = greeting()
    
    greeting_label = tk.Label(window, text=greeting_message, font=("Arial", 20), fg="black", bg="#add8e6")
    greeting_label.pack(expand=True)
    
    window.mainloop()

if __name__ == "__main__":
    show_greeting()
