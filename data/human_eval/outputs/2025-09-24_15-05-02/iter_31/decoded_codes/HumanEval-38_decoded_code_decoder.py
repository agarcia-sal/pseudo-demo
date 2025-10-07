from typing import List


def encode_cyclic(input_string: str) -> str:
    groups: List[str] = []
    length = len(input_string)
    group_count = (length + 2) // 3
    for index in range(group_count):
        start = 3 * index
        end = min(start + 3, length)
        groups.append(input_string[start:end])
    groups = [
        group[1:] + group[0] if len(group) == 3 else group
        for group in groups
    ]
    return ''.join(groups)


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))