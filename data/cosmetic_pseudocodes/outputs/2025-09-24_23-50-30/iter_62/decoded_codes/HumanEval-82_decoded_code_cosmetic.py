from typing import Callable

def prime_length(wrapper: str) -> bool:
    total_chars: int = len(wrapper)
    if total_chars <= 1:
        return False

    def check_divisor(index: int) -> bool:
        if index >= total_chars:
            return True
        if total_chars % index == 0:
            return False
        return check_divisor(index + 1)

    return check_divisor(2)