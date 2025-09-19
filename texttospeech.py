import tkinter as tk
import pyttsx3

# Initialize TTS engine
engine = pyttsx3.init()

def speak_text():
    text = entry.get("1.0", tk.END).strip()  # Get text from box and remove extra spaces 
    if text:
        engine.say(text)
        engine.runAndWait()

# Create GUI window
root = tk.Tk()
root.title("Text to Speech Converter")
root.geometry("400x300")

# Label
label = tk.Label(root, text="Enter text below:", font=("Arial", 12))
label.pack(pady=10)

# Text Box
entry = tk.Text(root, height=8, width=40, font=("Arial", 12))
entry.pack(pady=20)

# Speak Button
button = tk.Button(root, text="Speak", command=speak_text, font=("Arial", 12), bg="lightblue")
button.pack(pady=10)

# Run GUI
root.mainloop()
