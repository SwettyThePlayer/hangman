# ❤️ Hangman Game

A simple Hangman game built with Python! Guess the hidden word one letter at a time, keep track of your lives, and try to win before it's game over. <3

## 🎮 About the Game

This project is a beginner-friendly implementation of the classic Hangman game.

The game randomly selects a word from a predefined list and hides its letters.  
The player must guess the word one letter at a time.  
Every incorrect guess costs one life, so choose wisely!

## ✨ Features
- Random Words: A random word is selected at the start of the game.
- Hidden Word: Correctly guessed letters are revealed.
- Lives System: The player starts with 6 lives.
- Heart Counter: Remaining lives are displayed using <3 hearts.
- Tried Letters: Keeps track of all previously guessed letters.
- Input Validation: Checks if the player enters exactly one character.
- Repeated Guess Detection: Prevents guessing the same letter twice.
- Win Condition: Guess all the letters before running out of lives.
- Lose Condition: The game ends when all 6 lives are lost, revealing the correct word.
## 🛠️ Built With
- Python 3
- Random module
## 🚀 How to Run
Clone the repository:  
> bash
```
git clone YOUR-REPOSITORY-LINK
```
Navigate to the project folder:
> bash
```
cd YOUR-PROJECT-FOLDER
```
Run the game:
> bash
```
python hangman.py
```

## 📚 Development Process

The game was developed in seven steps:

1. Hide the word – Created the hidden word mechanic.
2. One letter guess – Added the ability to guess one letter at a time.
3. Loop the game – Made the game run until the player wins or loses.
4. Lives – Introduced a lives counter.
5. Random words and checks – Added random word selection, input validation, and repeated-letter detection.
6. Game look – Improved the interface with heart-themed lives and a tried-letters display.
7. Letter-only check - The player can now only type letters
## 🎯 Available Words

The game currently chooses randomly from:

- python
- laptop
- football
- pizza
- faro
- keyboard
## 📖 What I Learned

Through this project, I practised:

- Variables and lists
- While loops and for loops
- If/else conditions
- User input
- String manipulation
- Random word selection
- Basic input validation

### Made with Python and a little bit of love. <3
