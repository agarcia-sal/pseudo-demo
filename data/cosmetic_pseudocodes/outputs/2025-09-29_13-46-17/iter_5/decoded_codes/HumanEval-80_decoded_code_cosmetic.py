from typing import Callable


def is_happy(string_input: str) -> bool:
    def check_triplet(pos: int) -> bool:
        if pos > len(string_input) - 3:
            return True
        if not (
            string_input[pos] != string_input[pos + 1]
            and string_input[pos + 1] != string_input[pos + 2]
            and string_input[pos] != string_input[pos + 2]
        ):
            return False
        return check_triplet(pos + 1)

    if len(string_input) < 3:
        return False
    return check_triplet(0)