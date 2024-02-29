"""
Changes 11/13/19:
1. Simplified win check in Coin Flip
2. Added check for <=$0 bets in all games
3. Win/lose communication now includes bet amount
4. Part of main function for game selection and user input
11/17/19:
1. Added question to play again

To do:
1. Finish main function
2. Retool game functions to ask for bet from within functions
3. Figure out why "1" for input wont work but "1." will
4. Figure out how to exit the program
"""

import random
money = 100
play_decision = "Yes"

print("Welcome to the Game Master 7000!")
print("Would you like to play? (Yes/No)")
print("(Enter 'Exit' at any time to quit)")
play_decision = input()
if (play_decision == "No") or (play_decision == "no"):
    exit()

while(play_decision == "Yes"):
    print("What game would you like to play?")
    print("1. Coin Flip, 2. Cho Han, 3. Pick a Card, 4. Roulette")
    print("Please enter the number of your game.")
    game_selection = input()
    if (game_selection == str(1)) or (game_selection == "1."):
        print("You've selected Coin Flip! How much would you like to bet?" \
            " You currently have " + str(money) + " money.")
        bet = input()
        print("Heads or Tails?")
        pick = input()
        coin_flip(bet, pick)
        print("Would you like to play another game? (Yes/No)")
        play_decision = input()
    elif (game_selection == str(2)) or (game_selection == "2."):
        print("You've selected Cho Han! How much would you like to bet?" \
            " You currently have " + str(money) + " money.")
        bet = input()
        print("Odd or Even?")
        pick = input()
        cho_han(bet,pick)
        print("Would you like to play another game? (Yes/No)")
        play_decision = input()
    elif (game_selection == str(3)) or (game_selection == "3."):
        print("You've selected Pick a Card! How much would you like to bet?" \
            " You currently have " + str(money) + " money.")
        bet = input()
        pick_a_card(bet)
        print("Would you like to play another game? (Yes/No)")
        play_decision = input()
    elif (game_selection == str(4)) or (game_selection == "4."):
        print("You've selected Roulette! How much would you like to bet?" \
            " You currently have " + str(money) + " money.")
        bet = input()
        print("Single tile, Odd/Even, High/Low, Red/Black?")
        pick = input()
        roulette(bet,pick)
        print("Would you like to play another game? (Yes/No)")
        play_decision = input()
    elif (game_selection == "Exit"):
        exit()
    else:
        print("Game not recognized")



#Write your game of chance functions here
def coin_flip(bet, pick):
    print("Welcome to coin flip!")

    #Check to make sure bet is correct value
    if(bet <= 0):
        print("Your bet should be above 0")
        return bet
    print("You picked " + str(pick) + "!")
    random_flip = random.randint(1,2)

    #Tell user what the coin flip result was
    if (random_flip == 1):
        print("The coin flip came up Heads!")
    else:
        print("The coin flip came up Tails")

    #Simplified this section, no need to translate, just merged into one compare
    if (pick == "Heads") and (random_flip == 1):
        print("You win " + str(bet) + " dollars!")
        return bet
    elif (pick == "Tails") and (random_flip == 0):
        print("You win " + str(bet) + " dollars!")
        return (-bet)
    else:
        print("Sorry you lose " + str(bet) + " dollars")
        return -bet


def cho_han(bet, pick):
    print("Welcome to Cho-Han!")
    if(bet <= 0):
        print("Your bet should be above 0")
        return bet
    print("You picked " + str(pick) + "!")
    #Roll the dice!
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    #Tell the user what was rolled
    print ("The dice rolled a " + str(dice1) + " and a " + str(dice2) + "!")
    #Determine winner
    if (pick == "Odd") and ((dice1 + dice2)%2 == 1):
        print("You win " + str(bet) + " dollars!")
        return bet
    elif (pick == "Even") and ((dice1 + dice2)%2 == 0):
        print("You win " + str(bet) + " dollars!")
        return bet
    else:
        print("Sorry you lose " + str(bet) + " dollars")
        return (-bet)


def pick_a_card(bet):
    print("Welcome to Pick a card!")
    if(bet <= 0):
        print("Your bet should be above 0")
        return bet
    #Set list of cards, and set player1's card off first list
    cards = [1,2,3,4,5,6,7,8,9,10]
    player_card  = cards[random.randint(0,9)]
    #Remove cardplayer1 picked, and set computer card from remaining
    cards_pick2 = [1,2,3,4,5,6,7,8,9,10]
    cards_pick2.pop(player_card-1)
    computer_card = cards_pick2[random.randint(0,8)]
    #Determine winner
    print("Player 1 picked a " + str(player_card) + " and the computer picked a "
    \ + str(computer_card))
    if (player_card > computer_card):
        print("You win " + str(bet) + " dollars!")
        return bet
    elif (player_card == computer_card):
        print("You tied with the computer!")
        return (0)
    else:
        print("Sorry you lose " + str(bet) + " dollars")
        return (-bet)

def roulette(bet, pick):
    print("Welcome to roulette!")
    if(bet <= 0):
        print("Your bet should be above 0")
        return bet
    print("You picked " + str(pick) + "!")
    winning_pick = random.randint(0,39)
    if winning_pick == 39:
        winning_pick == "00"

    print("The ball stopped on " + str(winning_pick) + "!")
    #Determine winner
    #Single check
    if (pick == winning_pick):
        print("You win! You picked the single, and won " + str(bet) + " dollars!")
        return (bet*35)
    #Odd/Even check
    elif (pick == "Odd") or (pick == "Even"):
        if (pick == "Odd") and ((winning_pick % 2) == 1):
            print("You win! You picked odd correctly, and won " + str(bet) +
            \ " dollars!")
            return (bet)
        elif (pick == "Even") and ((winning_pick % 2) == 0):
            print("You win! You picked even correctly, and won " + str(bet) +
            \ " dollars!")
            return (bet)
        else:
            print("Sorry you lose " + str(bet) + " dollars")
            return (-bet)
    #High/Low check
    elif (pick == "High") or (pick == "Low"):
        if (pick == "High") and (winning_pick >= 19):
            print("You win! You picked high correctly, and won " + str(bet) +
            \ " dollars!")
            return bet
        elif (pick == "Low") and (winning_pick < 19):
            print("You win! You picked low correctly and won " + str(bet) +
            \ " dollars!")
            return bet
        else:
            print("Sorry you lose " + str(bet) + " dollars")
            return (-bet)
    #Red/Black check
    elif (pick == "Red") or (pick == "Black"):
        if (pick == "Red") and ((winning_pick % 2) == 1):
            print("You win! You picked red correctly and won " + str(bet) +
            \ " dollars!")
            return (bet)
        elif (pick == "Black") and ((winning_pick % 2) == 0):
            print("You win! You picked black correctly and won " + str(bet) +
            \ " dollars!")
            return (bet)
        else:
            print("Sorry you lose " + str(bet) + " dollars")
            return (-bet)

#Call your game of chance functions here
#money += coin_flip(17,"Tails")
#money += roulette(15,"High")
#money += cho_han(10,"Odd")
#money += pick_a_card(17)
