from typing import Callable

def is_palindrome(phi: str) -> bool:
    def check_position(k: int, limit: int, flag: bool) -> bool:
        if k >= limit:
            return flag
        character_one = phi[k]
        character_two = phi[(limit * 2) - k]
        return check_position(k + 1, limit, flag and (character_one == character_two))
    return check_position(0, len(phi) // 2, True)