from typing import Dict

def count_distinct_characters(input_string: str) -> int:
    char_map: Dict[str, bool] = {}
    index: int = 0
    lowered_string: str = ""
    while index != len(input_string):
        lowered_string += input_string[index].lower()
        index += 1
    for ch in lowered_string:
        if ch not in char_map:
            char_map[ch] = True
    count: int = 0
    for _ in char_map.keys():
        count += 1
    return count