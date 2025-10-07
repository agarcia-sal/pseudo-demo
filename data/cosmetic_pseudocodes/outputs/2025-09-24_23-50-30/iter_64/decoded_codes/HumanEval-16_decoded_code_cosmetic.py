from typing import Sequence

def count_distinct_characters(observable_value: Sequence[str]) -> int:
    accumulator: list[str] = []
    iterator: int = 0
    while iterator < len(observable_value):
        current_element = observable_value[iterator].lower()
        if current_element not in accumulator:
            accumulator.append(current_element)
        iterator += 1
    return len(accumulator)