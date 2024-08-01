import random
words = ["apple", "banana", "orange", "grape", "pear", "peach", "mango", "lemon", "lime", "berry", "cherry", "melon", "kiwi", "plum", "apricot", "avocado", "fig", "guava", "papaya", "pomegranate"]
selected_word = random.choice(words)
underscores = ["_"] * len(selected_word)

max_incorrect_guesses = 6
incorrect_guesses = 0

def display_word(word):
    print(" ".join(word))

def update_word(selected_word, underscores, guess):
    for index, letter in enumerate(selected_word):
        if letter == guess:
            underscores[index] = letter

def display_hangman(incorrect_guesses):
    hangman_stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """
    ]
    print(hangman_stages[incorrect_guesses])

display_word(underscores)
display_hangman(incorrect_guesses)

while "_" in underscores and incorrect_guesses < max_incorrect_guesses:
    guess = input("Guess a letter: ").lower()
    if guess in selected_word:
        update_word(selected_word, underscores, guess)
    else:
        incorrect_guesses += 1
        print(f"Incorrect guess. You have {max_incorrect_guesses - incorrect_guesses} guesses left.")
    display_word(underscores)
    display_hangman(incorrect_guesses)

if "_" not in underscores:
    print("Congratulations! You guessed the word:", selected_word)
else:
    print("Sorry, you ran out of guesses. The word was:", selected_word)
