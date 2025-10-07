def correct_bracketing(brackets_string: str) -> bool:
    balance_tracker: int = 0
    position_index: int = 0
    length: int = len(brackets_string)
    while position_index < length:
        current_symbol: str = brackets_string[position_index]
        if current_symbol != "<":
            balance_tracker -= 1
        else:
            balance_tracker += 1
        if balance_tracker < 0:
            return False
        position_index += 1
    return balance_tracker == 0