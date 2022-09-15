""" #Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass
 """
import pandas as pd
data = pd.read_csv("./day26_list_comprehension/nato_phonetic_alphabet.csv")

#1. Create a dictionary
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
phonetic_dict = {row.letter: row.code for (index,row) in data.iterrows()}
#print (phonetic_dict)

#2. Create a list of the phonetic code words from a word that the user inputs.
#3. Use exceptions to catch wrong user entry and recursively recall function
def generate_phonetics():
    word = input("Input a word: ")
    try:
        output = [phonetic_dict[letter.upper()] for letter in word]
    except KeyError:
        print("Only letters in the alphabet please - try again.")
        generate_phonetics()
    else:
        print(output)

generate_phonetics()