import random

def choose_word():
    words = ['apple', 'banana', 'cherry', 'orange', 'grape']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    word = choose_word()
    guessed_letters = set()
    max_attempts = 6
    attempts = 0

    print("Welcome to Hangman!")
    while True:
        print(display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        elif len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!")
            if display_word(word, guessed_letters) == word:
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            print("Incorrect guess.")
            attempts += 1
            if attempts == max_attempts:
                print("Sorry, you're out of attempts. The word was:", word)
                break

        print("")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    hangman()