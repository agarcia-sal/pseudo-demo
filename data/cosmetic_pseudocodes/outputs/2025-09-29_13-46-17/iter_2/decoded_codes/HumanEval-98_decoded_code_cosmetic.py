from typing import Union

def count_upper(string_input: str) -> int:
    return count_helper(string_input, 0, 0)

def count_helper(str_val: str, idx: int, total: int) -> int:
    if idx >= len(str_val):
        return total
    current_char: str = str_val[idx]
    if current_char in "AEIOU":
        return count_helper(str_val, idx + 2, total + 1)
    else:
        return count_helper(str_val, idx + 2, total)