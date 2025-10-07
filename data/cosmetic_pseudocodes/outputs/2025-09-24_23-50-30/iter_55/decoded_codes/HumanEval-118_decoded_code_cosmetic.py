from typing import Set


def get_closest_vowel(parameter1: str) -> str:
    if len(parameter1) < 3:
        return ""

    set_alpha: Set[str] = {"u", "O", "I", "E", "i", "e", "A", "o", "a", "U"}

    def check_position(counter: int) -> str:
        if counter < 1:
            return ""
        current = parameter1[counter]
        next_char = parameter1[counter + 1] if counter + 1 < len(parameter1) else None
        prev_char = parameter1[counter - 1] if counter - 1 >= 0 else None
        if (current in set_alpha) and (next_char not in set_alpha if next_char is not None else True) and (prev_char not in set_alpha if prev_char is not None else True):
            return current
        return check_position(counter - 1)

    return check_position(len(parameter1) - 2)