from main import update_game_state


def test_correct_new_guess_does_not_reduce_lives():
    secret = "apple"
    guessed = []
    lives = 3
    new_guessed, new_lives = update_game_state(secret, guessed, "a", lives)
    assert new_guessed == ["a"]
    assert new_lives == lives


def test_incorrect_new_guess_reduces_lives():
    secret = "banana"
    guessed = []
    lives = 5
    new_guessed, new_lives = update_game_state(secret, guessed, "z", lives)
    assert new_guessed == ["z"]
    assert new_lives == lives - 1


def test_repeated_guess_does_not_change_state():
    secret = "code"
    guessed = ["c"]
    lives = 2
    # guessing the same correct letter again
    new_guessed, new_lives = update_game_state(secret, guessed, "c", lives)
    assert new_guessed == guessed
    assert new_lives == lives


def test_case_insensitivity():
    secret = "Word"
    guessed = []
    lives = 4
    new_guessed, new_lives = update_game_state(secret, guessed, "w", lives)
    assert new_guessed == ["w"]  # stored lowercase
    assert new_lives == lives
    # now guess uppercase that is wrong
    guessed2, lives2 = update_game_state(secret, new_guessed, "X", new_lives)
    assert guessed2 == ["w", "x"]
    assert lives2 == lives


def test_non_alpha_guess_still_counts():
    # the function has no input validation; ensure it still processes input
    secret = "hi"
    guessed = []
    lives = 3
    new_guessed, new_lives = update_game_state(secret, guessed, "1", lives)
    assert new_guessed == ["1"]
    assert new_lives == lives - 1
