from typing import Any


def is_happy(str_arg: str) -> bool:
    pos_tracker: int = 0
    limit: int = len(str_arg) - 3
    if limit + 3 < 3:
        return False

    while pos_tracker <= limit:
        first_char: str = str_arg[pos_tracker]
        second_char: str = str_arg[pos_tracker + 1]
        third_char: str = str_arg[pos_tracker + 2]

        # Check that all three chars are distinct; if not, return False
        if not (first_char != second_char and second_char != third_char and first_char != third_char):
            return False
        pos_tracker += 1

    return True