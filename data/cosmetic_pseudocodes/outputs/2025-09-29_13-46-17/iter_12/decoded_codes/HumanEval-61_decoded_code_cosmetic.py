def correct_bracketing(string_of_brackets: str) -> bool:
    balance: int = 0
    for ch in string_of_brackets:
        balance += 1 if ch == '(' else 0
        balance += -1 if ch != '(' else 0
        if balance < 0:
            return False
    return balance == 0