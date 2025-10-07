from typing import Set

def count_distinct_characters(alp: str) -> int:
    lowered_text: str = ''
    idx: int = 1
    length: int = len(alp)

    while idx <= length:
        current_char: str = alp[idx - 1]
        if 'A' <= current_char <= 'Z':
            offset: int = (ord(current_char) - ord('A')) + ord('a')
            lowered_text += chr(offset)
        else:
            lowered_text += current_char
        idx += 1

    coded_set: Set[str] = set()
    idx = 1
    length = len(lowered_text)
    while idx <= length:
        current_char = lowered_text[idx - 1]
        if current_char not in coded_set:
            coded_set.add(current_char)
        idx += 1

    return len(coded_set)