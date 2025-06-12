import random

# List of predefined words
words = ['apple', 'banana', 'grape', 'mango', 'peach']
word = random.choice(words)

# Setup
guessed_letters = []
tries = 6
display_word = ['_'] * len(word)

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses allowed.\n")

# Game loop
while tries > 0 and '_' in display_word:
    print("Word:", ' '.join(display_word))
    print("Guessed letters:", ', '.join(guessed_letters))

    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter. Try another one.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
        print("✅ Good guess!\n")
    else:
        tries -= 1
        print(f"❌ Incorrect! You have {tries} tries left.\n")

# End of game
if '_' not in display_word:
    print("🎉 Congratulations! You guessed the word:", word)
else:
    print("💀 Game Over! The word was:", word)
