from typing import List

def encode_cyclic(string_s: str) -> str:
    groups: List[str] = []
    length: int = len(string_s)
    num_groups: int = (length + 2) // 3  # number of groups of up to 3 chars

    for i in range(num_groups):
        start_index: int = 3 * i
        end_index: int = min(start_index + 3, length)
        group: str = string_s[start_index:end_index]
        if len(group) == 3:
            # rotate left by 1 character
            group = group[1:] + group[0]
        groups.append(group)

    return ''.join(groups)


def decode_cyclic(string_s: str) -> str:
    return encode_cyclic(encode_cyclic(string_s))