import random
from word import words
import string

def get_valid_word(words):
  word = random.choice(words)  # randomly chooses somthing from the list
  while '_' in word or ' ' in word:
    word = random.choice(words) 
 
  return word.upper()

def hangman():
  word = get_valid_word(words) 
  word_letters = set(word) # letters in the word
  alphabet = set(string.ascii_uppercase)
  used_letters = set() # what the user has guessed 

  lives = 10

  # geting user input
  while len(word_letters) > 0 and lives > 0:
    # letters used 
    print('You have used these letters: ', ''.join(used_letters))
    print('You have', lives, 'lives left !!! ' )

    # what current word is
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print('Current Word: ', ' '.join(word_list))

    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)
        print("-------")
      else:
        lives = lives - 1
        print('Letter is not in Word. ')
        print("-------")

    elif user_letter in used_letters:
      print('You have already used that character. Please try again. ')
      print("-------")
    else:
      print('Invalid character. Please try again')
  if lives == 0:
    print('You died, sorry. The word was: ', word)
  else:
    print('Yay!! You have guessed the word: ', word, "!!!")

hangman()