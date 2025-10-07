from typing import Set

def count_distinct_characters(input_string: str) -> int:
    container: Set[str] = set()
    for element in input_string.lower():
        container.add(element)
    return len(container)