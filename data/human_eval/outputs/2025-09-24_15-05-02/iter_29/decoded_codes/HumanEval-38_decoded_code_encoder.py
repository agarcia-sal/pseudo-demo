from typing import List


def encode_cyclic(input_string: str) -> str:
    groups: List[str] = []
    length = len(input_string)
    num_groups = (length + 2) // 3
    for index in range(num_groups):
        start_position = 3 * index
        end_position = min(3 * index + 3, length)
        group = input_string[start_position:end_position]
        groups.append(group)
    for i, group in enumerate(groups):
        if len(group) == 3:
            groups[i] = group[1:] + group[0]
    return ''.join(groups)


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))