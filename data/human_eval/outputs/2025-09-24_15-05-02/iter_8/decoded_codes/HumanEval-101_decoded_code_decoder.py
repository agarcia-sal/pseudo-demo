from typing import List

def words_string(input_string: str) -> List[str]:
    if not input_string:
        return []
    character_list: List[str] = []
    for character in input_string:
        if character == ',':
            character_list.append(' ')
        else:
            character_list.append(character)
    joined_string: str = ''.join(character_list)
    return joined_string.split()