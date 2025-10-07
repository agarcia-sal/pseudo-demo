from typing import List


def words_string(input_string: str) -> List[str]:
    idx: int = 0
    tmp_chars: List[str] = []
    while idx < len(input_string):
        curr_ch: str = input_string[idx]
        if curr_ch == ',':
            tmp_chars.append(' ')
        else:
            tmp_chars.append(curr_ch)
        idx += 1

    if not tmp_chars:
        return []

    combined: str = ''
    pos: int = 0
    while pos < len(tmp_chars):
        combined += tmp_chars[pos]
        pos += 1

    return combined.split()