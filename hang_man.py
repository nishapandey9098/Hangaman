import random
from words import words
from lives_visual import lives_visual
import string

instruct_= """
*INSTRUCTIONS: 
This is how the hanged man looks like.
 +--------+
 O        |
/|\       |
/ \       |
          |
        =====

1) choose the random letter from the english alphabets
2) toal 6 chances are given to guess the word correctly
3) for the incorrect input the body parts will get removed gradually
4) GOOD LUCK!!! play smartly.
"""
def main():
    print("WELCOME TO HANG_A_MAN!!!")
    print("FOLLOW THE INSTRUCTIONS!!!")
    print(instruct_)
    hangman()
   
    

def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 6

    # take user input
    while len(word_letters) > 0 and lives > 0 :
        # letters used
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # current word is
        wordinlist = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual[6-lives])
        print('Current word: ', ' '.join(wordinlist))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here if no life is left or to get the result
    if lives == 0:
        print(lives_visual[6-lives])
        print('Current word: ', ' '.join(wordinlist))
        print('You died, sorry. The word was', word)
    else:
        print('CONGRATULATIONS! You guessed the word', word, '!!')
        print('Current word: ', ' '.join(wordinlist))



if __name__ == '__main__':
    main() 