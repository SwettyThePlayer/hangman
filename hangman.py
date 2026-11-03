import random

words = ["python", "laptop", "football", "pizza", "faro", "keyboard"]
word = random.choice(words)
guessed = []
lives = 6

print("=== HANGMAN GAME ===")

while True:
    display = ""
    for letter in word:
        if letter in guessed:
            display = display + letter + " "
        else:
            display = display + "_ "
    print()
    print(display)
    print("Lives: " + "<3 " * lives)
    print("Tried: " + ", ".join(guessed))

    if "_" not in display:
        print(f"You found it with {lives} lives! GG!")
        break
    if lives == 0:
        print(f"Game over! The word was {word}")
        break

    guess = input("Guess a letter: ").lower()
    if len(guess) != 1:
        print("Type ONE letter!")
        continue
    if guess in guessed:
        print("You already tried that!")
        continue
    if not guess.isalpha():
        print("Please type a letter!")
        continue
    guessed.append(guess)

    if guess in word:
        print("Yes!")
    else:
        lives = lives -1
        print("No!")