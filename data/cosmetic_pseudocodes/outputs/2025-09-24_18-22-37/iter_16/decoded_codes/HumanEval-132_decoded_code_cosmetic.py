from typing import List

def is_nested(strng: str) -> bool:
    opener_ids: List[int] = []
    closer_ids: List[int] = []
    idx: int = 0
    length: int = len(strng)
    while idx < length:
        ch: str = strng[idx]
        if ch == '[':
            opener_ids.append(idx)
        else:
            closer_ids.append(idx)
        idx += 1

    closer_ids.reverse()
    matched_count: int = 0
    pos_ptr: int = 0
    clos_len: int = len(closer_ids)

    for open_id in opener_ids:
        if pos_ptr < clos_len and open_id < closer_ids[pos_ptr]:
            matched_count += 1
            pos_ptr += 1

    return matched_count >= 2