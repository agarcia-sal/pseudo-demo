from typing import Set

def count_distinct_characters(string_input: str) -> int:
    char_set: Set[str] = set()
    index_counter: int = 0
    lowered_string: str = string_input.lower()

    while index_counter < len(lowered_string):
        char_set.add(lowered_string[index_counter])
        index_counter += 1

    return len(char_set)