# General plan:
# Give player two cards
# Have 4 of each card, so if player or dealer gets one, they have less chance of getting same
# Have "hit/stick" ability
# GIVE USER CHOICE OF HAVING ACE BE 1 OR 11!

# MAKE THIS CODE NEATER BY USING FUNCTIONS! (Maybe make a new branch for this)
# todo Allow dealer to draw fourth card.
# todo If player is dealt a card, that card should be removed from deck. So less chance of getting it next time!
# todo Ability to play again
# todo (ADVANCED FEATURE) Add ability to bet
# todo (ADVANCED FEATURE) Add suits

import numpy as np

deck = ['A', 'A', 'A', 'A', 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
        8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 'J', 'J', 'J', 'J',
        'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K']


def stick():
    print('Stick, got it')
    print('The value of your hand is {}'.format(hand_value))
    print('The value of the dealer\'s hand is {}'.format(dealer_hand_value))
    if hand_value > dealer_hand_value:
        print('You win!')
    else:
        print('Dealer wins!')


def card_value(card):
    if card in range(2, 11):
        card_value = card
    # If card is Ace, assign value to 11
    # todo Give player choice of using Ace as 1 or 11
    if card == 'A':
        card_value = 11
    # If card is J/Q/K
    if card in ['J', 'Q', 'K']:
        card_value = 10
    return card_value


card1_index = np.random.randint(52)
card2_index = np.random.randint(52)

# print('The randomly generated index for card 1 is {}'.format(card1_index))
# print('The randomly generated index for card 2 is {}'.format(card2_index))

card1 = deck[card1_index]
card2 = deck[card2_index]

print('First card is a {}'.format(card1))
print('Second card is a {}'.format(card2))

# assign card values
card1_value = card_value(card1)
card2_value = card_value(card2)

# #VALUE OF YOUR HAND
hand_value = card1_value + card2_value
print('The value of your hand is {}'.format(hand_value))

# #DEALER HAND
dealer1_index = np.random.randint(52)
dealer2_index = np.random.randint(52)

dealer1 = deck[dealer1_index]
dealer2 = deck[dealer2_index]

# #ASSIGNING DEALER CARD 1 VALUEs
dealer1_value = card_value(dealer1)
dealer2_value = card_value(dealer2)

# #VALUE OF DEALER HAND
dealer_hand_value = dealer1_value + dealer2_value
print('Dealer hand value (just here for debugging) is {}'.format(dealer_hand_value))

# Dealer drawing a third card
if dealer_hand_value < 15:
    print('dealer is drawing a third card (just here for debugging)')
    dealer3_index = np.random.randint(52)
    dealer3 = deck[dealer3_index]

    # #ASSIGNING DEALER 3 VALUE
    dealer3_value = card_value(dealer3)

    # #NEW VALUE OF DEALER HAND
    dealer_hand_value += dealer3_value
    print('New dealer hand value is {}'.format(dealer_hand_value))

    if dealer_hand_value > 21:
        print('Dealer is bust!')
        print('You win!')
        quit()  # this makes the program end as soon as dealer loses

# HIT OR STICK
print('Hit, or stick?', end=' ')
user_input = input()

if user_input.lower() == 'hit':
    print('Ok partner, third card coming up')
    card3_index = np.random.randint(52)
    card3 = deck[card3_index]
    print('Third card is a {}'.format(card3))

    # #ASSIGNING CARD 3 VALUE
    card3_value = card_value(card3)

    hand_value += card3_value
    print('The value of your hand is now {}'.format(hand_value))
    if hand_value > 21:
        print('Bust! Too bad.')

    if hand_value <= 21:
        print('Hit, or stick?')
        user_input = input()

        if user_input.lower() == 'hit':
            print('Ok partner, fourth card coming up')
            card4_index = np.random.randint(52)
            card4 = deck[card4_index]
            print('Fourth card is a {}'.format(card4))

            # ASSIGNING CARD 4 VALUE
            card4_value = card_value(card4)

            hand_value += card4_value
            print('The value of your hand is now {}'.format(hand_value))
            if hand_value > 21:
                print('Bust! Too bad.')

    elif user_input.lower() == 'stick':
        stick()

elif user_input.lower() == 'stick':
    stick()