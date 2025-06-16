import random

def hangman():
    words = ["python", "developer", "hangman", "challenge", "program"]
    word = random.choice(words)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    while True:
        # Show current guessed state of the word
        display_word = ' '.join([letter if letter in guessed_letters else '_' for letter in word])
        print("\nWord: " + display_word)
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        print("Guessed letters: " + ', '.join(sorted(guessed_letters)))

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word correctly!")
            print(f"The word was '{word}'.")
            break

        if incorrect_guesses >= max_incorrect:
            print("\nGame Over! You've reached the maximum number of incorrect guesses.")
            print(f"The word was '{word}'. Better luck next time!")
            break

        guess = input("Enter a letter to guess: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabetical letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is NOT in the word.")
            incorrect_guesses += 1

if __name__ == "__main__":
    hangman()

