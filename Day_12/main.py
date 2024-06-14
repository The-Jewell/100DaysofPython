#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

#sets difficulty of the game (amount of turns)
def set_difficulty(selected_difficulty):
  if selected_difficulty == "easy".lower():
    return 10
  elif selected_difficulty == 'hard'.lower():
    return 5
  else:
    return 0 

#checks guess against random number 
def compare_numbers(user_guess, random_number):
  if user_guess == random_number:
    print(f"You win. The number was {random_number}")
  elif user_guess > random_number:
    print("Too high.")
  elif user_guess < random_number:
    print("Too low.")
  else:
    print("Please enter a valid number.")

#game logic 
def game():
  #chose a random number between 1 and 100 
  random_number = random.randint(1,100)
  
  #print logo
  print(logo)
  print("Welcome to 'Guess the Number'!")
  print("I'm thinking of a number between 1 and 100.")
  #setting guess amount
  guess_amount = set_difficulty(input("Choose a difficulty. Type 'easy' or 'hard': "))
  #continuing the game  while the user has guesses left 
  while guess_amount > 0:
    print(f"You have {guess_amount} guesses left. ")
    user_guess = int(input("Make a guess: "))
    compare_numbers(user_guess, random_number)
    guess_amount -= 1 
  #ending the game if user is out of guesses 
  if guess_amount == 0 and user_guess != random_number:
    print(f"You ran out of guesses. You lose. The number was {random_number}")

#starting up the game 
game()
    