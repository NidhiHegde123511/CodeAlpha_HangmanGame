import random

# Step 1: Word list
words = ["python", "flask", "code", "alpha", "pandas"]

# Step 2: Randomly select a word
word = random.choice(words)

# Step 3: Game setup
guessed_letters = []
attempts = 6
display = ["_"] * len(word)

print("🎮 Welcome to Hangman! 🎮")
print("Guess the word:")

# Step 4: Game loop
while attempts > 0 and "_" in display:
    print("\nWord:", " ".join(display))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("🔁 You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        attempts -= 1
        print(f"❌ Wrong! You have {attempts} tries left.")

# Step 5: End of game
if "_" not in display:
    print("\n🎉 You won! The word was:", word)
else:
    print("\n💀 You lost. The word was:", word)
