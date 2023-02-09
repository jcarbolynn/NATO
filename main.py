import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# create a new dictionary from a dataframe, go row by row using .iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def make_NATO_happy():
  word = input("Enter a word: ").upper()
  try:
    output_list = [phonetic_dict[letter] for letter in word]
  except KeyError:
    print("Sorry, only letters in the alphabet please")
    # to repeat if user typed in something this cant interpret call function again not just this line: word = input("Enter a word: ").upper()
    make_NATO_happy()
  else:
    print(output_list)

make_NATO_happy()
