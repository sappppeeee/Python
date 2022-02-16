import random

def play():
  user = input("'R' For Rock, 'P' for Paper, 'S' for Scissors: ")
  computer = random.choice(['r','p','s'])

  if user == computer:
    return 'It\'s a tie'
  
  if is_win(user, computer):
    return 'You Won!'

  return 'You lost!'

def is_win(player, opponent):
  if (player =='r' and opponent == 's') or (player =='s' and opponent == 'p') or (player == 'p' and opponent == 'r'):
    return True

print(play())