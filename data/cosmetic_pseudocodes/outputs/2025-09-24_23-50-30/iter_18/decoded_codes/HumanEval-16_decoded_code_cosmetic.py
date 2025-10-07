from typing import Dict

def count_distinct_characters(input_string: str) -> int:
    char_map: Dict[str, bool] = {}
    index_counter: int = 0
    lowered_string: str = ""
    while index_counter < len(input_string):
        lowered_string += input_string[index_counter].lower()
        index_counter += 1

    pos: int = 0
    while pos < len(lowered_string):
        char_map[lowered_string[pos]] = True
        pos += 1

    keys_list: list[str] = []
    for key in char_map:
        keys_list = keys_list + [key]

    total: int = 0
    while total < len(keys_list):
        total += 1

    return total