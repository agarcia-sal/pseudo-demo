def correct_bracketing(string_of_brackets: str) -> bool:
    balance: int = 0
    pos: int = 0
    while pos < len(string_of_brackets):
        current_char: str = string_of_brackets[pos]

        if current_char != "(":
            balance -= 1
        else:
            balance += 1

        if balance < 0:
            return False

        pos += 1

    return balance == 0