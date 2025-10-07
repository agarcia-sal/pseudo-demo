from typing import List


def string_sequence(integer_n: int) -> str:
    accumulator: List[str] = []
    counter: int = 0
    while counter <= integer_n:
        element: str = str(counter)
        accumulator.append(element)
        counter += 1
    return " ".join(accumulator)