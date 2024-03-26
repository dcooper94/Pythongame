import random

def choose_word(category):
    file_path = f'{category.lower()}.txt'
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '_' for letter in word)

def display_hangman(incorrect_guesses):
    stages = [
        """
           _______
          |       |
          |       O
          |      /|\\
          |      / \\
         _|_
        |   |______
        |__________|
        """,
        """
           _______
          |       |
          |       O
          |      /|\\
          |      /
         _|_
        |   |______
        |__________|
        """,
        """
           _______
          |       |
          |       O
          |      /|\\
          |
         _|_
        |   |______
        |__________|
        """,
        """
           _______
          |       |
          |       O
          |      /|
          |
         _|_
        |   |______
        |__________|
        """,
        """
           _______
          |       |
          |       O
          |
          |
         _|_
        |   |______
        |__________|
        """,
        """
           _______
          |       |
          |
          |
          |
         _|_
        |   |______
        |__________|
        """,
        """
           _______
          |
          |
          |
          |
         _|_
        |   |______
        |__________|
        """
    ]
    return stages[incorrect_guesses]

def hangman():
    categories = ['Animals', 'Fruits', 'Countries']  # Add more categories as needed
    print("Welcome to Hangman!")
    print("Choose a category:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    category_choice = input("Enter the number corresponding to your desired category: ")
    try:
        category_choice = int(category_choice)
        if 1 <= category_choice <= len(categories):
            category = categories[category_choice - 1]
            word = choose_word(category)
        else:
            print("Invalid category choice. Please try again.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    guessed_letters = set()
    max_attempts = 6
    attempts = 0

    print("You have chosen the category:", category)
    while True:
        current_display = display_word(word, guessed_letters)
        print(current_display)
        print(display_hangman(attempts))
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
            current_display = display_word(word, guessed_letters)
            if current_display == word:
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            print("Incorrect guess.")
            attempts += 1
            if attempts == max_attempts:
                print("Sorry, you're out of attempts. The word was:", word)
                print(display_hangman(attempts))
                break

        print("")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    hangman()
