from typing import Callable


def correct_bracketing(string_of_brackets: str) -> bool:
    def Auxiliary_Recurse(index: int, balance: int) -> bool:
        if index >= len(string_of_brackets):
            return balance == 0
        current_char = string_of_brackets[index]
        updated_balance = balance + 1 if current_char == "(" else balance - 1
        if updated_balance < 0:
            return False
        return Auxiliary_Recurse(index + 1, updated_balance)

    return Auxiliary_Recurse(0, 0)