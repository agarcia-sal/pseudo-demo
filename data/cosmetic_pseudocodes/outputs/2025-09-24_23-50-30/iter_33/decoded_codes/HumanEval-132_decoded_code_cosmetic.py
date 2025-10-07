from typing import List


def is_nested(string: str) -> bool:
    start_indices: List[int] = []
    end_indices: List[int] = []
    for idx in range(len(string)):
        if string[idx] == '[':
            start_indices.append(idx)
        else:
            end_indices.append(idx)
    end_indices.reverse()

    match_count = 0
    cursor = 0
    total_ends = len(end_indices)

    for opening_pos in start_indices:
        if cursor < total_ends and opening_pos < end_indices[cursor]:
            match_count += 1
            cursor += 1

    return match_count >= 2