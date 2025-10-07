def correct_bracketing(string_of_brackets: str) -> bool:
    balance: int = 0
    for current_char in string_of_brackets:
        if current_char == "(":
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False
    return balance == 0