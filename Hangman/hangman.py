import hangman_words
import random 

from hangman_art import logo, stages
print(logo)

end_of_game = False

chosen_word = random.choice(hangman_words.word_list)
word_len = len(chosen_word)
lives = 6

#print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_len):
    display += '_'


while not end_of_game:
    guess = input("Guess a letter.\n").lower()

    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(
            f"You guessed {guess}, which isn't in the word. YOU LOSE A LIFE")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("")
            print(f"YOU LOSE. The word was '{chosen_word}'")

    print(f"{' '.join(display)}")

    if '_' not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
