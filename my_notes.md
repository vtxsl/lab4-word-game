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

# CoPilot Suggestions

## App States
## App Variables
## App Rules and Invariants
## App Bugs