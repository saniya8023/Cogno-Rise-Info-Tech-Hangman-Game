# Hangman Game

A text-based Hangman game built in Python. The application processes user guesses, tracks remaining attempts, dynamically updates the secret word hidden behind underscores, and visualizes the player's progress using terminal-based ASCII art.

This project was developed as part of my Python Developer internship at CognoRise InfoTech.

---

## Features

- **Dynamic Visual Feedback:** Uses a predefined list of multi-line ASCII art strings to draw the hangman state progressively with every incorrect guess.
- **Accurate Letter Tracking:** Leverages Python's built-in `enumerate` function to find and reveal all instances of a correctly guessed letter within the word.
- **State Management:** Keeps real-time track of correct guesses (using an underscore list) and incorrect attempts to determine win/loss conditions.
- **Case Normalization:** Evaluates user inputs in lower case to ensure consistency and prevent accidental misses due to capitalization.

---

## Built With

- Python 3.x
- `random` module: For selecting a random word from a predefined list of fruits.

---

## How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/saniya8023/CognoRise-Info-Tech-Hangman-Game.git](https://github.com/saniya8023/CognoRise-Info-Tech-Hangman-Game.git)
