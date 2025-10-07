from typing import List


def is_nested(input_str: str) -> bool:
    start_indices: List[int] = []
    end_indices: List[int] = []
    idx: int = 0

    while idx < len(input_str):
        if input_str[idx] == '[':
            start_indices.append(idx)
        else:
            end_indices.append(idx)
        idx += 1

    end_indices.reverse()

    matched_pairs: int = 0
    end_pointer: int = 0
    total_end: int = len(end_indices)

    for open_pos in start_indices:
        if end_pointer < total_end and open_pos < end_indices[end_pointer]:
            matched_pairs += 1
            end_pointer += 1

    return matched_pairs >= 2