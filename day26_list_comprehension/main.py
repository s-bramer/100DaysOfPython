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
print (phonetic_dict)

#2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Input a word: ")
output = [phonetic_dict[letter.upper()] for letter in word]
#output = [phonetic_dict.values for letter in word if letter == phonetic_dict.keys ]
print(output)