import random
import tkinter as tk
from tkinter import messagebox

def choose_word():
    words = ["python", "hangman", "developer", "challenge", "computer", "programming"]
    return random.choice(words)

def update_display():
    display_text.set(" ".join(letter if letter in guessed_letters else "_" for letter in word))

def guess_letter():
    guess = entry.get().lower()
    entry.delete(0, tk.END)
    
    if len(guess) != 1 or not guess.isalpha():
        messagebox.showwarning("Invalid Input", "Please enter a single letter.")
        return
    
    if guess in guessed_letters:
        messagebox.showinfo("Already Guessed", "You already guessed that letter.")
        return
    
    guessed_letters.add(guess)
    
    if guess in word:
        update_display()
        if all(letter in guessed_letters for letter in word):
            messagebox.showinfo("Congratulations!", f"You guessed the word: {word}")
            root.quit()
    else:
        global attempts
        attempts -= 1
        attempts_text.set(f"Attempts left: {attempts}")
        if attempts == 0:
            messagebox.showerror("Game Over", f"The word was: {word}")
            root.quit()

def start_game():
    global word, guessed_letters, attempts
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    update_display()
    attempts_text.set(f"Attempts left: {attempts}")

root = tk.Tk()
root.title("Hangman Game")

word = choose_word()
guessed_letters = set()
attempts = 6

display_text = tk.StringVar()
attempts_text = tk.StringVar()
update_display()

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, textvariable=display_text, font=("Arial", 24)).pack()
tk.Label(frame, textvariable=attempts_text, font=("Arial", 14)).pack()

entry = tk.Entry(frame, font=("Arial", 14))
entry.pack(pady=10)

guess_button = tk.Button(frame, text="Guess", command=guess_letter, font=("Arial", 14))
guess_button.pack()

start_game()
root.mainloop()




