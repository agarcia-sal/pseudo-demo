from typing import List


def encode_cyclic(s: str) -> str:
    groups: List[str] = []
    length: int = len(s)
    group_count: int = (length + 2) // 3  # Number of groups of size up to 3

    for i in range(group_count):
        start_index: int = 3 * i
        end_index: int = min(start_index + 3, length)
        group: str = s[start_index:end_index]
        groups.append(group)

    for index in range(len(groups)):
        group = groups[index]
        if len(group) == 3:
            groups[index] = group[1:] + group[0]

    return "".join(groups)


def decode_cyclic(s: str) -> str:
    return encode_cyclic(encode_cyclic(s))