from typing import List

def encode_cyclic(s: str) -> str:
    groups: List[str] = []
    length = len(s)
    num_groups = (length + 2) // 3  # Number of 3-char groups, including partial at end if any
    for i in range(num_groups):
        start = 3 * i
        end = min(start + 3, length)
        group = s[start:end]
        groups.append(group)
    for idx, group in enumerate(groups):
        if len(group) == 3:
            groups[idx] = group[1:] + group[0]
    return ''.join(groups)

def decode_cyclic(s: str) -> str:
    return encode_cyclic(encode_cyclic(s))