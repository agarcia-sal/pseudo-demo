from typing import Dict

def count_distinct_characters(input_string: str) -> int:
    unique_elements: Dict[str, bool] = {}

    def accumulate_characters(index: int) -> None:
        if index >= len(input_string):
            return
        current_char = input_string[index].lower()
        unique_elements[current_char] = True
        accumulate_characters(index + 1)

    accumulate_characters(0)

    distinct_count = 0
    for character in unique_elements:
        distinct_count += 1

    return distinct_count