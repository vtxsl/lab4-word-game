import random
# def update_game_state(secret_word: str, guessed_letters: list[str], guess: str, lives: int) -> tuple[list[str], int]:
#     guess = guess.lower()
#     secret_word = secret_word.lower()
#     new_guessed_letters = guessed_letters + [guess] if guess not in guessed_letters else guessed_letters

#     is_wrong = guess not in secret_word
#     is_new = guess not in guessed_letters
    
#     new_lives = lives - 1 if is_wrong and is_new else lives

#     return new_guessed_letters, new_lives

def play_game():
    word = random.choice(["python", "epita", "software", "logic", "code"])
    guessed = []
    lives = 6

    while lives > 0:
        display = [char if char in guessed else "_" for char in word]
        print(f"\nWord: {' '.join(display)}")
        print(f"Lives: {lives} | Guessed: {', '.join(guessed)}")
        
        if "_" not in display:
            print("You won!")
            return

        user_input = input("Guess a letter: ").lower()
        
        if len(user_input) == 1 and user_input.isalpha():
            guessed, lives = update_game_state(word, guessed, user_input, lives)
        else:
            print("Invalid input.")

    print(f"You lost! The word was: {word}")

play_game()