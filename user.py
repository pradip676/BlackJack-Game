# Use randint to generate random cards. 
# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from random import randint

# Write all of your code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
user_hand = 0
drawn_count = 0

while drawn_count < 2:
  card_rank = randint(1, 13)
  if card_rank == 1:
    card_name = 'Ace'
    user_hand = user_hand + 11
  elif card_rank == 11:
    card_name = 'Jack'
    user_hand = user_hand + 10
  elif card_rank == 12:
    card_name = 'Queen'
    user_hand = user_hand + 10
  elif card_rank == 13:
    card_name = 'King'
    user_hand = user_hand + 10
  else:
    card_name = card_rank
    user_hand = user_hand + card_rank

  print('Drew a ' + str(card_name))

  drawn_count = drawn_count + 1

while user_hand < 21 and input('You have ' + str(user_hand) + '. Hit (y/n)? ') == 'y':
  card_rank = randint(1, 13)
  if card_rank == 1:
    card_name = 'Ace'
    user_hand = user_hand + 11
  elif card_rank == 11:
    card_name = 'Jack'
    user_hand = user_hand + 10
  elif card_rank == 12:
    card_name = 'Queen'
    user_hand = user_hand + 10
  elif card_rank == 13:
    card_name = 'King'
    user_hand = user_hand + 10
  else:
    card_name = card_rank
    user_hand = user_hand + card_rank

  print('Drew a ' + str(card_name))

print('Final hand: ' + str(user_hand) + '.')
if user_hand == 21:
  print('BLACKJACK!')
elif user_hand > 21:
  print('BUST.')