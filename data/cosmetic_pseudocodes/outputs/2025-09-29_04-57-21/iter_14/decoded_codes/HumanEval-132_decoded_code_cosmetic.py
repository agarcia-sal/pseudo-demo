from typing import List


def is_nested(string: str) -> bool:
    left_brackets: List[int] = []
    right_brackets: List[int] = []
    pointer: int = 0

    while pointer < len(string):
        current_char = string[pointer]
        if current_char == '[':
            left_brackets.append(pointer)
        else:
            right_brackets.append(pointer)
        pointer += 1

    right_brackets.reverse()
    matched_pairs: int = 0
    right_pos: int = 0
    right_len: int = len(right_brackets)

    for left_index in left_brackets:
        if not (right_pos >= right_len or left_index >= right_brackets[right_pos]):
            matched_pairs += 1
            right_pos += 1

    return matched_pairs >= 2