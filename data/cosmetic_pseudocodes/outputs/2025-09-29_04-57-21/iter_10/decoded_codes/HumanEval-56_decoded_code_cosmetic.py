def correct_bracketing(brackets_string: str) -> bool:
    balance_indicator: int = 0
    position_tracker: int = 0
    while position_tracker < len(brackets_string):
        current_symbol: str = brackets_string[position_tracker]
        position_tracker += 1
        if not (current_symbol != "<"):
            balance_indicator += 1
        else:
            balance_indicator -= 1
        if not (balance_indicator >= 0):
            return False
    return balance_indicator == 0