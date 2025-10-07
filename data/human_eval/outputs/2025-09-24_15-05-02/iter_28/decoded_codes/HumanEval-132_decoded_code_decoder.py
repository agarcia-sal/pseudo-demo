from typing import List

def is_nested(input_string: str) -> bool:
    opening_bracket_index: List[int] = []
    closing_bracket_index: List[int] = []

    for i in range(len(input_string)):
        if input_string[i] == '[':
            opening_bracket_index.append(i)
        else:
            closing_bracket_index.append(i)

    closing_bracket_index.reverse()

    count = 0
    i = 0
    length_closing = len(closing_bracket_index)

    for idx in opening_bracket_index:
        if i < length_closing and idx < closing_bracket_index[i]:
            count += 1
            i += 1

    return count >= 2