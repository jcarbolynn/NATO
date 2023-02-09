import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# not organized the way we want
# cant do .to_dict():
# print(data.to_dict())
# print(type(data)

# data is a data frame so we can go through it row by row with iterrows
# get each value by column name by going into row.column_name
# for (index, row) in data.iterrows():
#   print(row.letter, row.code)

# create a new dictionary from a dataframe, go row by row using .iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)
# use keys to get to values
# print(phonetic_dict['K'])

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
# [new_item for item in list]
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
