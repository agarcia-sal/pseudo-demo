from typing import Sequence


def is_happy(tokens: Sequence[str]) -> bool:
    if len(tokens) < 3:
        return False

    def check_triplet(pos: int) -> bool:
        if pos > len(tokens) - 3:
            return True
        first, second, third = tokens[pos], tokens[pos + 1], tokens[pos + 2]
        if first == second or second == third or first == third:
            return False
        return check_triplet(pos + 1)

    return check_triplet(1)