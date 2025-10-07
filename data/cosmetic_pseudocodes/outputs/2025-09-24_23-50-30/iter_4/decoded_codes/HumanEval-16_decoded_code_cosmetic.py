from typing import Dict

def count_distinct_characters(input_string: str) -> int:
    characters_list: list[str] = []

    def gather_chars(index: int) -> None:
        if index >= len(input_string):
            return
        characters_list.append(input_string[index].lower())
        gather_chars(index + 1)

    gather_chars(0)

    unique_chars: Dict[str, bool] = {}
    for char in characters_list:
        unique_chars[char] = True

    return len(unique_chars)