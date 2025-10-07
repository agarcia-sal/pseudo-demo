from typing import List

def words_string(alphanumeric_sequence: str) -> List[str]:
    if not alphanumeric_sequence:
        return []

    buffer_chars: List[str] = []
    idx: int = 0
    while idx < len(alphanumeric_sequence):
        curr_char: str = alphanumeric_sequence[idx]
        if curr_char == ',':
            buffer_chars.append(' ')
        else:
            buffer_chars.append(curr_char)
        idx += 1

    composed_text: str = ""
    i: int = 0
    while i < len(buffer_chars):
        curr_item: str = buffer_chars[i]
        composed_text += curr_item
        i += 1

    return composed_text.split(' ')