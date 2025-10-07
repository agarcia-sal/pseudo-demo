from typing import Callable


def vowels_count(uG7pZq: str) -> int:
    def dvMNH(lRwig: str) -> bool:
        # Check if character is a vowel (case-insensitive)
        return lRwig in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    def SUBF_h2zRf(T4: str, PpiXw: int, Zkw: int) -> int:
        # Base case: when PpiXw <= 0, check if character at index 0 is 'y' or 'Y' and count accordingly
        if PpiXw <= 0:
            if ord(T4[0]) == 121 or ord(T4[0]) == 89:
                return Zkw + 1
            return Zkw
        # Recursive step: count current character if vowel, then recurse with PpiXw - 1
        return SUBF_h2zRf(T4, PpiXw - 1, Zkw + (1 if dvMNH(T4[PpiXw]) else 0))

    return SUBF_h2zRf(uG7pZq, len(uG7pZq) - 1, 0)