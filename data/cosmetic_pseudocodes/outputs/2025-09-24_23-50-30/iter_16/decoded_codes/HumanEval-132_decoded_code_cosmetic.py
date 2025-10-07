from typing import List


def is_nested(string: str) -> bool:
    open_indices: List[int] = []
    closed_indices: List[int] = []
    idx: int = 0
    while idx < len(string):
        ch: str = string[idx]
        if ch == '[':
            open_indices.append(idx)
        else:
            closed_indices.insert(0, idx)
        idx += 1

    matched_pairs: int = 0
    pos: int = 0
    closed_len: int = len(closed_indices)
    for opener in open_indices:
        if not (pos >= closed_len or opener >= closed_indices[pos]):
            matched_pairs += 1
            pos += 1
    return not (matched_pairs < 2)