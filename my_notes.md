# My Original Thinking

### What are the states of a game like Hangman?
**Start/Setup:** Choosing a random word and initializing variables.
**Playing:** The main loop where the user provides input and the display updates.
**Won:** The user successfully guessed all letters before running out of lives.
**Lost:** The user ran out of lives before guessing the word.

### What variables are required?
`secret_word` (string): The word to be guessed.
`guessed_letters` (list): A collection of all letters the user has tried.
`lives` (int): The number of attempts remaining (defaulting to 6).
`masked_word` (string): The current representation of the word (e.g., `_ _ S _ E`).

### What are the rules and invariants?
The game ends when `lives` reaches 0 or all letters in `secret_word` are in `guessed_letters`.
Only unique letters should be added to the list of guessed letters.
`lives` only decreases if the guessed letter is not in the `secret_word` and has not been guessed before.

### What kind of bugs and edge cases should we be careful about?
Handling uppercase vs. lowercase input (case sensitivity).
Preventing users from entering numbers or multiple characters at once.
Ensuring the same correct or incorrect letter isn't penalized twice.
Handling empty input or whitespace.

### New Feature implementation NO AI YET

Implement a list of letters and pop after the computer guesses it.
create a function that actually guesses the letters.
make the whole game a loop somehow to keep asking after.
potentially make a priority list of letters so vowels first and then consonents with the least common ones being late.
implementing a difficulty feature to specify the amount of lives for the computer to guess from.
