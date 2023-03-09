
from python_tests.wordle import wordle


def test_incorrect_guess():
    result = wordle("ropes", "child")
    assert result == "00000"


def test_correct_guess():
    result = wordle("angry", "angry")
    assert result == "22222"


def test_only_first_character_correct():
    result = wordle("angry", "aaaaa")
    assert result == "20000"


def test_first_character_wrong():
    result = wordle("bbbbb", "aaaaa")
    assert result == "00000"


def test_only_different_first_character_correct():
    result = wordle("bngry", "bbbbb")
    assert result == "20000"


def test_bbbbb_is_not_always_the_right_answer():
    result = wordle("ccccc", "bbbbb")
    assert result == "00000"
