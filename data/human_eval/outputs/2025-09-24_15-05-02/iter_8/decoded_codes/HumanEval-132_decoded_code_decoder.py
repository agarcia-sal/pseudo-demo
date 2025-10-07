from typing import List


def is_nested(string: str) -> bool:
    opening_bracket_indices: List[int] = []
    closing_bracket_indices: List[int] = []
    for i, char in enumerate(string):
        if char == '[':
            opening_bracket_indices.append(i)
        else:
            closing_bracket_indices.append(i)
    closing_bracket_indices.reverse()

    count = 0
    i = 0
    closing_length = len(closing_bracket_indices)
    for opening_idx in opening_bracket_indices:
        if i < closing_length and opening_idx < closing_bracket_indices[i]:
            count += 1
            i += 1
    return count >= 2