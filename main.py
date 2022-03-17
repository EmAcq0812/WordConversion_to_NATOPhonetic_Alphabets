import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pd.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
dict3 = {"A": "Alfa", "B": "Bravo"}
nato_data = pd.read_csv('nato_phonetic_alphabet.csv')
# print(nato_data)

nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
# print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
a_word = True

user_word = input('Key in your word:  ').upper()
code_words = []

code_code = [nato_dict[let] for let in user_word if let in nato_dict.keys()]
print(code_code)

# print(nato_dict.keys())
#
# for let in code_words:
#     if let in nato_dict.keys():
#         print(let)


# Similar code as above

# for letters in user_word:
#     if letters in nato_dict.keys():
#         code_words.append(nato_dict[letters])
# print(code_words)
