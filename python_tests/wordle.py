def wordle(target, guess):
    code = "00000"

    if (guess[0] == target[0]):
        code = "20000"

    if target == guess:
        code = "22222"

    return code
