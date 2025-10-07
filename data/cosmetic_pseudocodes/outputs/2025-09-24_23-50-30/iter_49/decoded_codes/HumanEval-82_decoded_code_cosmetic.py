from typing import Callable


def prime_length(input_string: str) -> bool:
    def check_divisor(candidate_divisor: int, max_limit: int) -> bool:
        if candidate_divisor >= max_limit:
            return True
        if max_limit % candidate_divisor == 0:
            return False
        return check_divisor(candidate_divisor + 1, max_limit)

    total_chars: int = len(input_string)
    if total_chars <= 1:
        return False
    return check_divisor(2, total_chars)