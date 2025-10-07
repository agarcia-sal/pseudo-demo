from typing import List


def words_string(string_input: str) -> List[str]:
    if not string_input:
        return []
    character_list: List[str] = []
    for character in string_input:
        if character == ',':
            character_list.append(' ')
        else:
            character_list.append(character)
    joined_string: str = ''.join(character_list)
    return joined_string.split()