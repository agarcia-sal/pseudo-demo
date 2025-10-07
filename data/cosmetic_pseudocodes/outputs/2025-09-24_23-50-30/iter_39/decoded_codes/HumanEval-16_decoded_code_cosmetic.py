from typing import Set

def count_distinct_characters(str_arg: str) -> int:
    accumulator: Set[str] = set()
    index: int = 0
    limit: int = len(str_arg)
    while index < limit:
        symbol = str_arg[index].lower()
        if symbol not in accumulator:
            accumulator.add(symbol)
        index += 1
    return len(accumulator)