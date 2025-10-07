from typing import List


def is_nested(input_string: str) -> bool:
    openings: List[int] = []
    closings: List[int] = []
    idx: int = 0

    while idx < len(input_string):
        if input_string[idx] == '[':
            openings.append(idx)
        else:
            closings.append(idx)
        idx += 1

    closings.reverse()
    match_count: int = 0
    closings_pos: int = 0
    closings_len: int = len(closings)

    for curr_idx in openings:
        if closings_pos < closings_len and curr_idx < closings[closings_pos]:
            match_count += 1
            closings_pos += 1

    return match_count >= 2