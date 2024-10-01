
from random import randint

print("-----------")
print("YOUR TURN")
print("-----------")

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

print("-----------")
print("DEALER TURN")
print("-----------")

dealer_hand = 0
drawn_count = 0

while dealer_hand <= 17:
    if drawn_count >= 2:
        print('Dealer has ' + str(dealer_hand) + '.')

    card_rank = randint(1, 13)
    if card_rank == 1:
        card_name = 'Ace'
        dealer_hand = dealer_hand + 11
    elif card_rank == 11:
        card_name = 'Jack'
        dealer_hand = dealer_hand + 10
    elif card_rank == 12:
        card_name = 'Queen'
        dealer_hand = dealer_hand + 10
    elif card_rank == 13:
        card_name = 'King'
        dealer_hand = dealer_hand + 10
    else:
        card_name = card_rank
        dealer_hand = dealer_hand + card_rank

    print('Drew a ' + str(card_name))

    drawn_count = drawn_count + 1

print('Final hand: ' + str(dealer_hand) + '.')
if dealer_hand == 21:
    print('BLACKJACK!')
elif dealer_hand > 21:
    print('BUST.')

print("-----------")
print("GAME RESULT")
print("-----------")

# working with user hand and dealer hand

if dealer_hand > 21 and user_hand > 21 or dealer_hand == 21 and user_hand == 21 or (user_hand == dealer_hand):
    print("Tie.")

# line 110 to 118 is used to compare if user didn't draw any cards and decided to use his final hand before he wins or lose with if dealer hands value is >=17 and < 21. 

elif dealer_hand < 21 and dealer_hand >= 17 and user_hand <21:
    
    if dealer_hand > user_hand:
        print("Dealer wins!")
    else:
        print("You win!")
    
elif user_hand > 21:    # user busts, so dealer always wins in this case
    print("Dealer wins!")

elif dealer_hand == 21:   #black jack so dealer wins. Already checked the condition in line 103 for tie. 
    print("Dealer wins!")

else:
    print("You win!") # line 107 to 120 says all the condtion when dealer wins , so using else will directly give our condition when user wins)





        
    

    