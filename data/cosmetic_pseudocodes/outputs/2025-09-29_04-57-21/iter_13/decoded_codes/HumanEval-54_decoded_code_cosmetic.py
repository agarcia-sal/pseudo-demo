from typing import List

def same_chars(string_zero: str, string_one: str) -> bool:
    def gather_unique_chars(text: str) -> List[str]:
        unique_map: dict[str, bool] = {}
        index = 0
        length = len(text)
        while index < length:
            current_character = text[index]
            unique_map[current_character] = True
            index += 1
        return list(unique_map.keys())

    first_unique = gather_unique_chars(string_zero)
    second_unique = gather_unique_chars(string_one)

    if len(first_unique) != len(second_unique):
        return False

    checker: dict[str, bool] = {}
    for char_element in first_unique:
        checker[char_element] = True

    for char_element in second_unique:
        if char_element not in checker:
            return False

    return True