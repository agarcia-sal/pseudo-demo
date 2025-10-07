from typing import List


def is_nested(text: str) -> bool:
    left_indices: List[int] = []
    right_indices: List[int] = []
    current_pos: int = 0
    text_limit: int = len(text) - 1

    while current_pos <= text_limit:
        if text[current_pos] == '[':
            left_indices.append(current_pos)
        else:
            right_indices.append(current_pos)
        current_pos += 1

    right_indices.reverse()

    found_pairs: int = 0
    right_pos: int = 0
    right_length: int = len(right_indices)

    left_counter: int = 0
    while left_counter < len(left_indices):
        if right_pos < right_length:
            if left_indices[left_counter] < right_indices[right_pos]:
                found_pairs += 1
                right_pos += 1
        left_counter += 1

    return found_pairs >= 2