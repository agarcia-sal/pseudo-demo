from typing import Dict

def count_distinct_characters(input_string: str) -> int:
    unique_letters: Dict[str, bool] = {}
    idx: int = 0
    str_len: int = len(input_string)
    while idx < str_len:
        current_char: str = input_string[idx].lower()
        unique_letters[current_char] = True
        idx += 1
    return len(unique_letters)