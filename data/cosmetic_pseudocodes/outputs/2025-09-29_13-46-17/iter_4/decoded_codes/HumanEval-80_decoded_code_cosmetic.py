from typing import Callable


def is_happy(string_input: str) -> bool:
    def check_triplet(pos: int) -> bool:
        if pos > len(string_input) - 3:
            return True

        c1, c2, c3 = string_input[pos], string_input[pos + 1], string_input[pos + 2]

        if not (c1 != c2 and c2 != c3 and c1 != c3):
            return False
        return check_triplet(pos + 1)

    if len(string_input) < 3:
        return False
    return check_triplet(0)