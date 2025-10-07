from typing import List

def count_distinct_characters(string_input: str) -> int:
    accumulator: List[str] = []
    index_counter: int = 0
    transformed_string: List[str] = list(string_input.lower())

    while index_counter < len(transformed_string):
        char = transformed_string[index_counter]
        if char not in accumulator:
            accumulator.append(char)
        index_counter += 1

    return len(accumulator)