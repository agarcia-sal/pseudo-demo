from typing import Set

def count_distinct_characters(parameter_string: str) -> int:
    converted_string: str = "".join(c.lower() for c in parameter_string)
    unique_characters_set: Set[str] = set()
    index: int = 0
    while index < len(converted_string):
        current_char = converted_string[index]
        if current_char not in unique_characters_set:
            unique_characters_set.add(current_char)
        index += 1
    result_count: int = len(unique_characters_set)
    return result_count