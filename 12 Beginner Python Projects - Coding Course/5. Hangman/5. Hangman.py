from curses import use_env
import random
from word import words
import string

def get_valid_word(words):
  word = random.choice(words)
  while '_' in word or ' ' in word:
    word = random.choice(words)
 
  return word.upper()

def hangman():
  word = get_valid_word(words)
  word_letters = set(word)
  alphabet = set(string.ascii_uppercase)
  use_letters = set()