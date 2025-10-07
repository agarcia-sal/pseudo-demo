from typing import List


def encode_cyclic(input_string: str) -> str:
    groups: List[str] = []
    n = len(input_string)
    group_count = (n + 2) // 3  # number of groups of size 3 (may have smaller last group)
    for i in range(group_count):
        start_index = 3 * i
        end_index = min(3 * i + 3, n)
        groups.append(input_string[start_index:end_index])
    for i, group in enumerate(groups):
        if len(group) == 3:
            groups[i] = group[1:] + group[0]
    return ''.join(groups)


def decode_cyclic(encoded_string: str) -> str:
    return encode_cyclic(encode_cyclic(encoded_string))