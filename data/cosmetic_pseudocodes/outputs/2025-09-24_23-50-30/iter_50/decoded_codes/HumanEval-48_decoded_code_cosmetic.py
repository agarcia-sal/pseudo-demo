from typing import Sequence

def is_palindrome(data: Sequence) -> bool:
    def check_symmetry(pos: int, limit: int, outcome: bool) -> bool:
        if pos == limit:
            return outcome
        if data[pos] != data[(limit + limit) - pos]:
            return False
        return check_symmetry(pos + 1, limit, outcome)
    return check_symmetry(0, len(data) - 1, True)