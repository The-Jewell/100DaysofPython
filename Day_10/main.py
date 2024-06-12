from art import logo



#calculator 
#add
def add(n1, n2):
  return n1 + n2

#subtract
def subtract(n1 ,n2):
  return n1 - n2

#multiply 
def multiply(n1 ,n2):
  return n1 * n2

#divide
def divide(n1 ,n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  }
def caclulator():
  print(logo)
  more_calculations = True
  num1 = float(input("What is the first number?: "))
  for symbol in operations:
    print(symbol)
  while more_calculations:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}") 
  
  
    should_continue = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation.")
    if should_continue == "n".lower():
      more_calculations = False 
      caclulator()
    else: 
      num1 = answer

caclulator()
  
  