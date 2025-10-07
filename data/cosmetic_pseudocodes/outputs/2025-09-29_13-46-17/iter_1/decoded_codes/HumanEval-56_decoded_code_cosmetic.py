def correct_bracketing(brackets_string: str) -> bool:
    balance: int = 0
    for char in brackets_string:
        if char == "<":
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False
    return balance == 0