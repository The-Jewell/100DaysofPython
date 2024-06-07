#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random_letters = []
random_symbols = []
random_numbers = []

#pick random letters 
for letter in range(1, nr_letters + 1):
  random_letter = random.choice(letters)
  random_letters.append(random_letter)
# print(random_letters)

#pick random symbols
for symbol in range(1, nr_symbols + 1):
  random_symbol = random.choice(symbols)
  random_symbols.append(random_symbol)
# print(random_symbols)

#pick random numbers
for number in range(1, nr_numbers + 1):
  random_number = random.choice(numbers)
  random_numbers.append(random_number)
# print(random_numbers)
#combine all random lists
random_password = random_letters + random_symbols + random_numbers
#print(random_password)

#randomize order of random password characters
randomized_password = random.sample(random_password, len(random_password))

#convert final password into a string
randomized_password_str = ""
for character in randomized_password:
  randomized_password_str += character

print(f"Your password could be: {randomized_password_str}")
  