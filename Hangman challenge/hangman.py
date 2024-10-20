import random

# Predefined list of words
words_list = ['python', 'hangman', 'challenge', 'development', 'programming']

# Function to display the word with guessed letters
def display_word(word, guesses):
    return ' '.join([letter if letter in guesses else '_' for letter in word])

# Main hangman game function
def hangman_game():
    word = random.choice(words_list)  # Randomly select a word from the list
    guessed_letters = []              # List to store guessed letters
    attempts_left = 6                 # Maximum number of incorrect guesses

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    
    while attempts_left > 0:          # Loop until attempts run out
        print(f"\nWord: {display_word(word, guessed_letters)}")  # Display the current state of the word
        print(f"Attempts left: {attempts_left}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        
        guess = input("Enter a letter: ").lower()  # Player input for guessing a letter
        
        if len(guess) != 1 or not guess.isalpha():  # Validate the input
            print("Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters:                # Check if letter has already been guessed
            print("You've already guessed that letter.")
        elif guess in word:                         # Check if the guess is correct
            guessed_letters.append(guess)
            if set(guessed_letters) >= set(word):   # Win condition: all letters guessed
                print(f"\nCongrats! You guessed the word: {word}")
                break
        else:                                       # Wrong guess, reduce attempts
            guessed_letters.append(guess)
            attempts_left -= 1
            print(f"Wrong guess! {guess} is not in the word.")
    
    if attempts_left == 0:                          # Loss condition: no attempts left
        print(f"Sorry, you've run out of attempts. The word was {word}.")

# Run the game
hangman_game()
