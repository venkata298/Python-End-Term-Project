import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr

def listen_to_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        try:
            message_label.config(text="Listening... Speak now")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)

            text = recognizer.recognize_google(audio)
            text_display.delete(1.0, tk.END)
            text_display.insert(tk.END, text)

            message_label.config(text="Speech recognized!")

        except sr.UnknownValueError:
            messagebox.showerror("Error", "Sorry, I did not understand the speech.")
            message_label.config(text="Couldn't understand the speech.")
        except sr.RequestError:
            messagebox.showerror("Error", "Speech service is unavailable.")
            message_label.config(text="Service unavailable.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            message_label.config(text="An error occurred.")

def open_speech_page():
    speech_window = tk.Toplevel()
    speech_window.title("Speech Recognition")
    speech_window.geometry("450x400")
    speech_window.configure(bg="#1E1E1E")

    speech_title_label = tk.Label(speech_window, text="Speech to Text Converter", font=("Arial", 18, "bold"), fg="#FFEB3B", bg="#1E1E1E")
    speech_title_label.pack(pady=10)

    welcome_msg = f"Hello User, let's convert your speech to text!"
    personalized_label = tk.Label(speech_window, text=welcome_msg, font=("Arial", 14), bg="#1E1E1E", fg="white")
    personalized_label.pack(pady=10)

    global message_label
    message_label = tk.Label(speech_window, text="Click 'Start Listening' to speak", font=("Arial", 14), bg="#1E1E1E", fg="white")
    message_label.pack(pady=10)

    global text_display
    text_display = tk.Text(speech_window, height=8, width=50, font=("Arial", 12), wrap=tk.WORD, bd=3, relief="sunken", fg="black")
    text_display.pack(pady=10)

    listen_button = tk.Button(speech_window, text="Start Listening", font=("Arial", 14), bg="#4CAF50", fg="white", command=listen_to_speech)
    listen_button.pack(pady=10, ipadx=10, ipady=5)

    retry_button = tk.Button(speech_window, text="Retry", font=("Arial", 14), bg="#FF5733", fg="white", command=lambda: text_display.delete(1.0, tk.END))
    retry_button.pack(pady=10, ipadx=10, ipady=5)

    back_button = tk.Button(speech_window, text="Back to Start", font=("Arial", 14), bg="#2196F3", fg="white", command=speech_window.destroy)
    back_button.pack(pady=10, ipadx=10, ipady=5)

    speech_window.mainloop()

def start_page():
    start_window = tk.Tk()
    start_window.title("Welcome to User's Speech-to-Text")
    start_window.geometry("450x400")
    start_window.configure(bg="#1E1E1E")

    welcome_label = tk.Label(start_window, text="Welcome to Speech-to-Text Converter", font=("Arial", 18, "bold"), fg="#FFEB3B", bg="#1E1E1E")
    welcome_label.pack(pady=30)

    greeting_label = tk.Label(start_window, text="Hello User!", font=("Arial", 14, "bold"), fg="#FFEB3B", bg="#1E1E1E")
    greeting_label.pack(pady=10)

    start_button = tk.Button(start_window, text="Start", font=("Arial", 14), bg="#4CAF50", fg="white", command=open_speech_page)
    start_button.pack(pady=20, ipadx=10, ipady=5)

    start_window.mainloop()

if __name__ == "__main__":
    start_page()
