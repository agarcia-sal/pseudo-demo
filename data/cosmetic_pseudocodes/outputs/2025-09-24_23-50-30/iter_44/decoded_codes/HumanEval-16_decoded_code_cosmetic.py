from typing import Set

def count_distinct_characters(scratchpad: str) -> int:
    accumulator: Set[str] = set()
    for index in range(len(scratchpad)):
        interim_char = scratchpad[index].lower()
        if interim_char not in accumulator:
            accumulator.add(interim_char)
    return len(accumulator)