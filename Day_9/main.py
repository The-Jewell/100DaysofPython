from replit import clear #import replit to use clear function 
from art import logo
#HINT: You can call clear() to clear the output in the console.
#function to add bidder 
def add_bidder(name, bid):
  bidders[name] = bid

#function to determine highest bidder 
def find_highest_bidder(bidding_record):
  highest_bid  = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
print(logo)
print('Welcome to the Secret Auction')

bidders = {}
#state tracking 
add_another_bidder = True

while add_another_bidder:
  name = input("What is your name?:")
  bid = int(input("What is your bidding amount?$"))
  add_bidder(name, bid)
  more_bidders = input("Are there any other bidders? type yes or no\n")
  clear()
  if more_bidders == "no".lower():
    add_another_bidder = False
    find_highest_bidder(bidders)
  
  
