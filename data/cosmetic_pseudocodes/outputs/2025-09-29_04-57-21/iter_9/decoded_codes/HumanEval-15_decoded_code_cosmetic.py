from typing import List


def string_sequence(integer_n: int) -> str:
    accumulator: List[str] = []
    iterator: int = 0
    while iterator <= integer_n:
        accumulator.append(str(iterator))
        iterator += 1
    return " ".join(accumulator)