import random
import string
from words import words

def valid_word(words):
    
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = valid_word(words) #gets a word for user to guess
    word_letters = set(word) #letters in word
    alphabet = set(string.ascii_uppercase) #varibale which checks if letter is in alphabet
    used_letters = set() #what letters have be used already

    lives = 10


    while len(word_letters) > 0 and lives > 0:

        #letters used
        print('You have', lives, 'lives life and you have used these letters: ', ' '.join(used_letters))

        #what the current word is with un - guessed letters left blank
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters: #if letter has not been used add it to list
            used_letters.add(user_letter)

            if user_letter in word_letters: #if letter is in the word then remove the letter from list
                word_letters.remove(user_letter)

            else:

                lives = lives - 1 #removes a life for incorrect guesses
                print('Chosen letter is NOT in the word')

        elif user_letter in used_letters:
            print('You have already guessed that letter. Try Again :(')

        else:
            print('Invalid Character ;(')

    # gets here when len(word) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was' , word)
    else:
        print('You guessed the word' , word, '!')


hangman()