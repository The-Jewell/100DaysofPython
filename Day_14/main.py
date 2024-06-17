#imports
from art import logo, vs
from game_data import data
import random 
# from replit import clear -- import used to clear terminal in replit 

#function that contains main game logic
def higher_or_lower():
  score = 0 
  game_over = False
  random_person_a = random_person()
  random_person_b = random_person()
  if random_person_a == random_person_b:
    random_person_b = random_person()
  print(logo)
  while not game_over:
    print(f"\n Compare A: {random_person_a['name']}, a {random_person_a['description']}, from {random_person_a['country']}")
    print(vs)
    print(f"\n Against B: {random_person_b['name']}, a {random_person_b['description']}, from {random_person_b['country']}")
    user_choice = input("\n Who has more followers? Type 'A' or 'B': ").lower()
    # clear() -- this clears terminal in replit 
    is_correct = check_answer(user_choice, random_person_a['follower_count'], random_person_b['follower_count'])
    if is_correct:
      score += 1
      print(f"You're Right! Current score: {score}")
      random_person_a = random_person_b
      random_person_b = random_person()   
    else: 
      game_over = True
      print(f"Sorry, that's wrong. Final Score: {score}")

#generates random people for comparison 
def random_person():
  person = random.choice(data)
  return person 
  
#checks user answer to see if it is the correct guess
def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
      

#start of game
higher_or_lower()



