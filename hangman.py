import random

words = ["python", "hangman", "coding", "simple", "random"]
word = random.choice(words)
guessed = set()
wrong = 0
max_wrong = 6

while wrong < max_wrong:
    display = " ".join(letter if letter in guessed else "_" for letter in word)
    print(f"\n{display}")
    print(f"Wrong guesses: {wrong}/{max_wrong} | Guessed: {sorted(guessed)}")

    if "_" not in display:
        print("You win!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter a single letter.")
        continue

    if guess in guessed:
        print("Already guessed.")
        continue

    guessed.add(guess)

    if guess not in word:
        wrong += 1
else:
    print(f"\nYou lose! The word was: {word}")