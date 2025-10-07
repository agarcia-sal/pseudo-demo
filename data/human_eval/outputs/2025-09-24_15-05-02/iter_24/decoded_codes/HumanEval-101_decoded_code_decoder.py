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
    joined_string: str = ''.join(s_list)
    words: List[str] = joined_string.split()
    return words