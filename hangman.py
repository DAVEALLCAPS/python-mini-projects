import random

# A list of easy animal words
words = [    "cat", "dog", "fish", "bird", "bear",
    "frog", "lion", "cow", "pig", "bee",
    "bat", "rat", "ant", "fox", "goat",
    "duck", "seal"]

# Randomly choose a word from the list
chosen_word = random.choice(words)

# Represent the word as a list of underscores
guessed_word = ["_"] * len(chosen_word)
attempts_left = 10
guessed_letters = []

def display_game_state():
    print(" ".join(guessed_word))
    print(f"Attempts left: {attempts_left}")
    print(f"Guessed letters: {' '.join(guessed_letters)}")

while attempts_left > 0 and "_" in guessed_word:
    display_game_state()
    
    # Player input
    guess = input("Guess a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please guess a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    
    guessed_letters.append(guess)

    # Check if guess is in the word
    if guess in chosen_word:
        for idx, letter in enumerate(chosen_word):
            if letter == guess:
                guessed_word[idx] = guess
    else:
        attempts_left -= 1

# Calculate attempts used
attempts_used = 10 - attempts_left

# End game messages
if "_" not in guessed_word:
    print(f"Congratulations! You guessed the word '{chosen_word}' in {attempts_used} attempts!")
else:
    print(f"You're out of attempts! The word was: {chosen_word}")
