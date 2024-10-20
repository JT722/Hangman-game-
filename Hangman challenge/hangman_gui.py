import random
import tkinter as tk

# Word list
words_list = ['python', 'hangman', 'challenge', 'development', 'programming']
word_to_guess = random.choice(words_list)

# Game state variables
guessed_letters = []
attempts_left = 6

# Function to update the display of the word
def update_word_display():
    display = ' '.join([letter if letter in guessed_letters else '_' for letter in word_to_guess])
    word_label.config(text=display)
    attempts_label.config(text=f"Attempts left: {attempts_left}")

# Function to process a letter guess
def guess_letter():
    global attempts_left
    letter = letter_entry.get().lower()

    if len(letter) != 1 or not letter.isalpha():
        result_label.config(text="Please enter a valid letter.")
    elif letter in guessed_letters:
        result_label.config(text="You've already guessed that letter.")
    elif letter in word_to_guess:
        guessed_letters.append(letter)
        result_label.config(text=f"Correct! {letter} is in the word.")
    else:
        guessed_letters.append(letter)
        attempts_left -= 1
        result_label.config(text=f"Wrong! {letter} is not in the word.")
    
    update_word_display()
    
    if attempts_left == 0:
        result_label.config(text=f"Game Over! The word was: {word_to_guess}")
        guess_button.config(state=tk.DISABLED)
    elif set(guessed_letters) >= set(word_to_guess):
        result_label.config(text=f"Congrats! You guessed the word: {word_to_guess}")
        guess_button.config(state=tk.DISABLED)

# Tkinter window setup
root = tk.Tk()
root.title("Hangman Game")

word_label = tk.Label(root, text="_ " * len(word_to_guess), font=("Helvetica", 24))
word_label.pack()

attempts_label = tk.Label(root, text=f"Attempts left: {attempts_left}")
attempts_label.pack()

letter_entry = tk.Entry(root)
letter_entry.pack()

guess_button = tk.Button(root, text="Guess", command=guess_letter)
guess_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

update_word_display()

root.mainloop()
