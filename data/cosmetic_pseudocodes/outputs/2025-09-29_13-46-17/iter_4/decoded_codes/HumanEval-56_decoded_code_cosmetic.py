from typing import Callable


def correct_bracketing(brackets_string: str) -> bool:
    def iterate_check(index: int, balance_amount: int) -> bool:
        if index >= len(brackets_string):
            return balance_amount == 0
        current_symbol = brackets_string[index]
        if current_symbol != "<":
            updated_balance = balance_amount - 1
        else:
            updated_balance = balance_amount + 1
        if updated_balance < 0:
            return False
        return iterate_check(index + 1, updated_balance)

    return iterate_check(0, 0)