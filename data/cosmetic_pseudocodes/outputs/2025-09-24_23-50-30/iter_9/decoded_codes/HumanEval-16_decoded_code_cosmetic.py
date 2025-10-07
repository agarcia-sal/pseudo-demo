from typing import Set

def count_distinct_characters(text_input: str) -> int:
    temp_set: Set[str] = set()
    index_counter: int = 0
    while index_counter < len(text_input):
        temp_set |= {text_input[index_counter].lower()}
        index_counter += 1
    return len(temp_set)