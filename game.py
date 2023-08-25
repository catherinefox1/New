import random

def choose_word():
    words = ["apple", "banana", "cherry", "grape", "orange", "pear", "pineapple", "strawberry"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    max_attempts = 6
    guessed_letters = []
    word = choose_word()
    
    print("Welcome to Hangman!")
    
    while max_attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print("Correct!")
            if display_word(word, guessed_letters) == word:
                print("\nCongratulations! You've guessed the word:", word)
                break
        else:
            max_attempts -= 1
            print("Incorrect guess. You have", max_attempts, "attempts left.")
    
    if max_attempts == 0:
        print("\nGame over! The word was:", word)

hangman()
