from typing import Iterable

def same_chars(firstInput: Iterable[str], secondInput: Iterable[str]) -> bool:
    charSetA = set(firstInput)
    charSetB = set(secondInput)
    return charSetA == charSetB