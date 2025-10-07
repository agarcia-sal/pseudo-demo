from typing import Dict

def count_distinct_characters(input_string: str) -> int:
    char_map: Dict[str, bool] = {}
    index: int = 0
    total_count: int = 0
    length_input: int = len(input_string)

    while index < length_input:
        current_char: str = input_string[index]
        normalized_char: str = current_char
        if 'A' <= normalized_char <= 'Z':
            normalized_char = chr(ord(normalized_char) + (ord('a') - ord('A')))
        if normalized_char not in char_map:
            char_map[normalized_char] = True
            total_count += 1
        index += 1

    return total_count