from typing import Literal


def correct_bracketing(string_of_brackets: str) -> bool:
    """
    Check if the input string_of_brackets consisting of '(' and ')' is correctly
    bracketed (balanced).

    Returns True if the brackets are balanced, False otherwise.
    """
    balance: int = 0
    for ch in string_of_brackets:
        if ch == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False  # closing bracket before matching opening
    return balance == 0