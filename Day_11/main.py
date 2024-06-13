############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   https://appbrewery.github.io/python-day11-demo/



import random
from art import logo
#commenting out replit - used to clear console
# from replit import clear 


def deal_card():
  """Returns a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)


def calculate_score(hand):
  """Takes a list of cardsa and calculates the score of the hand"""
  score = sum(hand)
  if score > 21:
    for card in hand:
      if card == 11:
        hand.remove(card)
        hand.append(1)
  return score


def compare(user_score, computer_score):
  """Compares the user score to the dealer score and returns the result"""
  if user_score == computer_score:
    return "It's a draw."
  elif user_score == 21:
    return "Blackjack! You win."
  elif user_score > 21:
    return "You lose."
  elif computer_score > user_score and computer_score <= 21:
    return "You lose."
  elif computer_score > 21:
    return "You win."
  elif user_score > computer_score and user_score < 21:
    return "You win."
  else:
    return "That was random"


def black_jack():
  """Main function of the game"""
  #turns game on, prints logo, and deals initial hand
  game_on = True
  print(logo)
  user_cards = []
  computer_cards = []
  for i in range(2):
    user_cards.append(deal_card())
  computer_cards.append(deal_card())

  #prints current hand and score, asks if the user wants to draw another card
  print(
      f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}"
  )
  print(f"Dealer's card showing: {calculate_score(computer_cards)}")

  #if user has backjack, user wins
  if calculate_score(user_cards) == 21:
    print("You win")
    #ask user if they want to play again
    play_again = input("Would you like to play again? Type 'y' or 'n': ")
    if play_again == "y".lower():
    #   clear()
      black_jack()
    else:
      print("Thanks for playing")
  #ask user if they want to draw another card
  hit_stand = input("Type 'HIT' to get another card or 'STAY' to pass: ")
  #if user wants to draw another card, deals another card and prints current hand and score
  while game_on:
    if hit_stand == "HIT".lower():
      user_cards.append(deal_card())
      print(
          f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}"
      )
      #checks if user has gone over 21, if so user loses, game ends
      if calculate_score(user_cards) > 21:
        print("BUST, You lose.")
        play_again = input("Would you like to play again? Type 'y' or 'n': ")
        if play_again == "y".lower():
          black_jack()
        else:
          print("Thanks for playing")
          game_on = False
      else:
        print(f"Dealer's card showing: {calculate_score(computer_cards)}")
        hit_stand = input(
            "Type 'HIT' to get another card or 'STAY' to pass: ")
    #once user is done drawing cards, computer(dealer) draws cards until score is at least 17
    else:
      while calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())
      #prints final score and result of the game - asks user if they want to play another game
      print(
          f"Your final cards: {user_cards}, final score: {calculate_score(user_cards)}"
      )
      print(
          f"Dealer's final cards: {computer_cards}, final score: {calculate_score(computer_cards)}"
      )
      print(
          compare(calculate_score(user_cards),
                  calculate_score(computer_cards)))
      play_again = input("Would you like to play again? Type 'y' or 'n': ")
      if play_again == "y".lower():
        black_jack()
      else:
        print("Thanks for playing")
        game_on = False


#initial call to start the game
black_jack()
