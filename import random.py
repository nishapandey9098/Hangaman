import random

def hangman():
    words = ['python', 'hangman', 'game', 'openai', 'programming']
    chosen_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    while True:
        print("\n")
        display_word = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(display_word)

        if display_word.replace(" ", "") == chosen_word:
            print("Congratulations! You guessed the word correctly!")
            break

        if attempts == 0:
            print("Sorry, you lost! The word was: " + chosen_word)
            break

        print("Attempts left:", attempts)
        guess = input("Enter a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You've already guessed that letter. Try again.")
            elif guess in chosen_word:
                guessed_letters.append(guess)
            else:
                attempts -= 1
                print("Wrong guess!")
                print_hangman(attempts)
        else:
            print("Invalid input. Please enter a single letter.")

def print_hangman(attempts):
    stages = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    print(stages[6-attempts])

hangman()
