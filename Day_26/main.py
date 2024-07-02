import pandas

np_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(np_data)

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
np_dict = {row.letter: row.code for (index,row) in np_data.iterrows()}
# print(np_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
is_running = True
while is_running:
    word = input("Enter a word: ").upper()
    try:
        output_list = [np_dict[letter] for letter in word]
    except KeyError:
        print("Please enter only letters.")
    else:
        print(output_list)
        is_running = False


