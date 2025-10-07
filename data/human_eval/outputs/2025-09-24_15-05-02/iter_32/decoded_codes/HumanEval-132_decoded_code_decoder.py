from typing import List

def is_nested(input_string: str) -> bool:
    opening_bracket_index: List[int] = []
    closing_bracket_index: List[int] = []
    for index in range(len(input_string)):
        if input_string[index] == '[':
            opening_bracket_index.append(index)
        else:
            closing_bracket_index.append(index)
    closing_bracket_index.reverse()

    count: int = 0
    i: int = 0
    length_closing: int = len(closing_bracket_index)
    for idx in opening_bracket_index:
        if i < length_closing and idx < closing_bracket_index[i]:
            count += 1
            i += 1
    return count >= 2