from typing import Literal

def correct_bracketing(string_of_brackets: str) -> bool:
    def check_balance(position: int, current_level: int) -> bool:
        if position > len(string_of_brackets):
            return current_level == 0
        if current_level < 0:
            return False
        symbol: Literal["(", ")"] = string_of_brackets[position - 1]
        adjusted_level = current_level + 1 if symbol == "(" else current_level - 1
        return check_balance(position + 1, adjusted_level)
    return check_balance(1, 0)