from typing import List


def encode_cyclic(input_string: str) -> str:
    groups: List[str] = []
    n = (len(input_string) + 2) // 3  # number of groups
    for index in range(n):
        start = 3 * index
        end = min(start + 3, len(input_string))
        groups.append(input_string[start:end])

    encoded_groups: List[str] = []
    for group in groups:
        if len(group) == 3:
            # rotate left by 1 character within the group
            encoded_groups.append(group[1:] + group[0])
        else:
            encoded_groups.append(group)

    return ''.join(encoded_groups)


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))