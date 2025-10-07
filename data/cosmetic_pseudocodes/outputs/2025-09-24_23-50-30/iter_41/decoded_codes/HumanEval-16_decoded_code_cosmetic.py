from typing import Set

def count_distinct_characters(param1: str) -> int:
    accumulator: Set[str] = set()
    iterator: int = 1
    limit: int = len(param1)
    while iterator <= limit:
        temp_char: str = param1[iterator - 1].lower()
        accumulator |= {temp_char}
        iterator += 1
    return len(accumulator)