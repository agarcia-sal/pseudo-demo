from typing import List

def encode_cyclic(s: str) -> str:
    groups: List[str] = []
    total_groups = (len(s) + 2) // 3
    for i in range(total_groups):
        start_index = 3 * i
        end_index = 3 * i + 3 if (3 * i + 3) < len(s) else len(s)
        group = s[start_index:end_index]
        groups.append(group)
    cycled_groups: List[str] = []
    for group in groups:
        if len(group) == 3:
            cycled_group = group[1:] + group[0]
            cycled_groups.append(cycled_group)
        else:
            cycled_groups.append(group)
    result = ''.join(cycled_groups)
    return result

def decode_cyclic(s: str) -> str:
    first_pass = encode_cyclic(s)
    second_pass = encode_cyclic(first_pass)
    return second_pass