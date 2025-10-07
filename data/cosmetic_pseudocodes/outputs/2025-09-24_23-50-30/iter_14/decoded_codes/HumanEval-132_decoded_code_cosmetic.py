from typing import List


def is_nested(string: str) -> bool:
    left_indices: List[int] = []
    right_indices: List[int] = []
    i: int = 0
    while i < len(string):
        if string[i] == '[':
            left_indices.append(i)
        else:
            right_indices.append(i)
        i += 1

    j: int = len(right_indices) - 1
    reversed_right: List[int] = []
    while j >= 0:
        reversed_right.append(right_indices[j])
        j -= 1

    matched_count: int = 0
    idx_right: int = 0
    while idx_right < len(reversed_right):
        if matched_count == len(left_indices):
            break
        if left_indices[matched_count] < reversed_right[idx_right]:
            matched_count += 1
            idx_right += 1
            continue
        idx_right += 1

    return matched_count >= 2