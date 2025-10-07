from typing import List

def words_string(s: str) -> List[str]:
    if not s:
        return []
    s_list: List[str] = []
    for letter in s:
        if letter == ',':
            s_list.append(' ')
        else:
            s_list.append(letter)
    replaced_str: str = ''.join(s_list)
    return replaced_str.split()