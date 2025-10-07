from typing import List


def words_string(s: str) -> List[str]:
    if not s:
        return []

    s_list: List[str] = []
    for character in s:
        if character == ',':
            s_list.append(' ')
        else:
            s_list.append(character)
    joined_string: str = ''.join(s_list)
    return joined_string.split()