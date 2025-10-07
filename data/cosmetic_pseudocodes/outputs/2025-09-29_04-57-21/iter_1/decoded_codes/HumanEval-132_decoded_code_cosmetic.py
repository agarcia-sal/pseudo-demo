from typing import List


def is_nested(string: str) -> bool:
    starts: List[int] = []
    ends: List[int] = []
    for i in range(len(string)):
        if string[i] == '[':
            starts.append(i)
        else:
            ends.append(i)
    ends.reverse()
    matched_pairs: int = 0
    idx: int = 0
    ends_len: int = len(ends)
    for start_pos in starts:
        if idx < ends_len and start_pos < ends[idx]:
            matched_pairs += 1
            idx += 1
    return matched_pairs >= 2