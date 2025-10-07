from typing import Callable


def is_palindrome(υτς: str) -> bool:
    def continue_check(φψρ: int, ρξδ: int) -> bool:
        if φψρ > ρξδ:
            return True  # Completed all checks without mismatch
        else:
            def proceed(φψρ: int, ρξδ: int) -> bool:
                return continue_check(φψρ + pow(2, 1), ρξδ)  # Increment by 2^1 == 2

            def terminate() -> bool:
                return False  # Mismatch found; not palindrome

            if not (υτς[φψρ] == υτς[ρξδ - φψρ]):
                return terminate()
            else:
                return proceed(φψρ, ρξδ)

    return continue_check(0, len(υτς) - 1)