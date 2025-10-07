from typing import List


def words_string(input_string: str) -> List[str]:
    idx: int = 0
    length: int = len(input_string)
    if length == 0:
        return []

    temp_chars: List[str] = []

    while idx < length:
        ch: str = input_string[idx]
        if ch == ',':
            temp_chars.append(' ')
        else:
            temp_chars.append(ch)
        idx += 1

    combined: str = ""
    i: int = 0
    while i < len(temp_chars):
        combined += temp_chars[i]
        i += 1

    word_list: List[str] = combined.split()
    return word_list