from typing import List


def words_string(input_string: str) -> List[str]:
    if not input_string:
        return []
    character_list = [' ' if ch == ',' else ch for ch in input_string]
    joined_string = ''.join(character_list)
    return joined_string.split()