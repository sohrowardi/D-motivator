import tkinter as tk
from tkinter import ttk
import random
from cryptography.fernet import Fernet

# Encryption key (replace 'your_key_here' with your actual key)
key = b'muPrZwxdmMHybsJNXhUP0HF9lMSf4_x8BkzhhZr-J6o='

# Initialize the Fernet cipher with the key
cipher = Fernet(key)

# Function to decrypt the contents of response_encrypted.txt
def decrypt_response():
    with open('response_encrypted.txt', 'rb') as file:
        encrypted_text = file.read()
        decrypted_text = cipher.decrypt(encrypted_text).decode()
        return decrypted_text

# Load the decrypted response and split it into lines
decrypted_response = decrypt_response().splitlines()

# Variable to store the previous input
previous_input = ""

# Function to display a random line from decrypted response
def display_text(event=None):
    global previous_input
    user_input = entry.get().strip()
    
    # Only display a new result if the input is different from the previous one
    if user_input != previous_input:
        previous_input = user_input
        random_response = random.choice(decrypted_response)
        output_text.config(text=random_response)

# Creating the main window
root = tk.Tk()
root.title("Motivator")

# Setting the style for the widgets
style = ttk.Style()
style.configure('TButton', font=('Arial', 12))
style.configure('TLabel', font=('Arial', 12))

# Creating and placing GUI elements
label = ttk.Label(root, text="Enter your problem:")
label.grid(row=0, column=0, padx=10, pady=10)

entry = ttk.Entry(root, width=40)
entry.grid(row=0, column=1, padx=10, pady=10)

button = ttk.Button(root, text="Motivate me!", command=display_text)
button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

output_text = ttk.Label(root, text="", wraplength=300)
output_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Binding the <Return> key to display_text function
root.bind('<Return>', display_text)

# Running the GUI
root.mainloop()
