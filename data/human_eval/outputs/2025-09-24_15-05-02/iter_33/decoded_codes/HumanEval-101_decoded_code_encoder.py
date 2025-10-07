from typing import List

def words_string(input_string: str) -> List[str]:
    if not input_string:
        return []
    temporary_list: List[str] = []
    for character in input_string:
        if character == ',':
            temporary_list.append(' ')
        else:
            temporary_list.append(character)
    joined_string = ''.join(temporary_list)
    return joined_string.split()