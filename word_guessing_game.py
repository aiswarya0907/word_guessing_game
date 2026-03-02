import random
word_bank = {
    "easy": {
        "Animals": {
            "Lion": "King of the jungle with a loud roar.",
            "Panda": "Black and white bear that eats bamboo.",
            "Penguin": "Flightless bird from Antarctica.",
            "Tiger": "Striped big cat that hunts alone."
        }
    },
    "medium": {
        "Countries": {
            "Japan": "Land of the rising sun.",
            "Brazil": "Home of the Amazon rainforest.",
            "Australia": "Known for kangaroos and the Outback.",
            "China": "Home of the Great Wall."
        }
    },
    "hard": {
        "Movies": {
            "Frozen": "A princess with ice powers.",
            "Coco": "A boys journey to the land of the dead",
            "Up": "An old man flies his house with balloons.",
            "Rocky": "An underdog boxer gets his big chance."
        }
    }
}

#Get user input 
level = input("Which level would you like to play? easy/medium/hard\n").lower()

if level not in word_bank:
    print("Level not found. Defaulting to easy.")
    level = "easy"

#Extract category and words
chosen_level = word_bank[level]
category = list(chosen_level.keys())[0]
words_dict = chosen_level[category]

# Pick a random word and its corresponding hint
word_key = random.choice(list(words_dict.keys()))
word = word_key.lower()
hint = words_dict[word_key]

guessedword = ["_"] * len(word)
attempts = 10

print("\nCategory:",category)
print("Hint:",hint)

#Loop
while attempts > 0:
    print("\nCurrent word: " + " ".join(guessedword))
    guess = input("Guess a letter: ").lower()

    # Basic check to ensure only one letter is entered
    if len(guess) != 1:
        print("Please enter only one letter.")
        continue

    if guess in word:
        print("Great guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessedword[i] = guess
    else:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}")

    if "_" not in guessedword:
        print(f"\nCongratulations!! You guessed the word: {word}")
        break

if attempts == 0 and "_" in guessedword:
    print(f"\nYou have run out of attempts! The word was: {word}")