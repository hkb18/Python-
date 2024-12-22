import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_phonetics_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [nato_phonetics_dict[letters] for letters in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please!")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
