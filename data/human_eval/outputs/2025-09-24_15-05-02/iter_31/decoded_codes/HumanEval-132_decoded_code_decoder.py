from typing import List

def is_nested(input_string: str) -> bool:
    opening_bracket_index: List[int] = []
    closing_bracket_index: List[int] = []
    for idx, ch in enumerate(input_string):
        if ch == '[':
            opening_bracket_index.append(idx)
        else:
            closing_bracket_index.append(idx)
    closing_bracket_index.reverse()
    count = 0
    i = 0
    length_to_check = len(closing_bracket_index)
    for idx in opening_bracket_index:
        if i < length_to_check and idx < closing_bracket_index[i]:
            count += 1
            i += 1
    return count >= 2