from typing import List


def is_nested(phrase: str) -> bool:
    start_indices: List[int] = []
    end_indices: List[int] = []
    for counter in range(len(phrase)):
        if phrase[counter] == '[':
            start_indices.append(counter)
        else:
            end_indices.append(counter)
    end_indices.reverse()

    tally: int = 0
    curr_pos: int = 0
    end_len: int = len(end_indices)
    for elem in start_indices:
        if curr_pos < end_len and elem < end_indices[curr_pos]:
            tally += 1
            curr_pos += 1
    return tally >= 2