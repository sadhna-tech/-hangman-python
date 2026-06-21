import random

words = [
    "python",
    "developer",
    "github",
    "hangman",
    "computer",
    "keyboard",
    "programming",
    "internet",
    "database",
    "algorithm"
]

word = random.choice(words)

guessed_letters = []
lives = 6

print("===== Hangman Game =====")

while lives > 0:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word.")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter a single letter only.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        lives -= 1
        print(f"Wrong guess! Lives left: {lives}")
    else:
        print("Correct!")

if lives == 0:
    print(f"\n💀 Game Over! The word was '{word}'.")