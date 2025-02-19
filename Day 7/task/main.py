import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
letter_amount = len(chosen_word)
number = 0
while number <=letter_amount:
    print("_", end=" ")
    number += 1

guess = input("\nGuess a letter: ").lower()

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

for letter in chosen_word:
    if letter == guess:
        print(letter, end=" ")
    else:
        print("_", end=" ")

