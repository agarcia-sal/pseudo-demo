def correct_bracketing(brackets_string: str) -> bool:
    balance_tracker: int = 0
    iterator: int = 0
    while iterator < len(brackets_string):
        current_char: str = brackets_string[iterator]
        if current_char == "<":
            balance_tracker += 1
        else:
            balance_tracker -= 1
        if balance_tracker < 0:
            return False
        iterator += 1
    return balance_tracker == 0