from typing import List

def words_string(s: str) -> List[str]:
    if not s:
        return []
    temp_list: List[str] = []
    for character in s:
        if character == ',':
            temp_list.append(' ')
        else:
            temp_list.append(character)
    combined_string = ''.join(temp_list)
    return combined_string.split()