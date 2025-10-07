from typing import List

def encode_cyclic(s: str) -> str:
    groups: List[str] = []
    length = len(s)
    group_count = (length + 2) // 3
    for i in range(group_count):
        start_index = 3 * i
        end_index = min(3 * i + 3, length)
        groups.append(s[start_index:end_index])
    cycled_groups: List[str] = []
    for group in groups:
        if len(group) == 3:
            cycled_group = group[1:] + group[0]
            cycled_groups.append(cycled_group)
        else:
            cycled_groups.append(group)
    return ''.join(cycled_groups)

def decode_cyclic(s: str) -> str:
    return encode_cyclic(encode_cyclic(s))