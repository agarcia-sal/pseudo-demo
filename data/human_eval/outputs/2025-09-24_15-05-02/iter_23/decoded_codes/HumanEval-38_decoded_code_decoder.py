from typing import List


def encode_cyclic(s: str) -> str:
    groups: List[str] = []
    length_s: int = len(s)
    # Calculate number of groups: ceil division of length_s by 3
    num_groups: int = (length_s + 2) // 3
    for i in range(num_groups):
        start_index: int = 3 * i
        end_index: int = min(start_index + 3, length_s)
        group: str = s[start_index:end_index]
        groups.append(group)
    for index in range(len(groups)):
        if len(groups[index]) == 3:
            groups[index] = groups[index][1:] + groups[index][0]
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    return encode_cyclic(encode_cyclic(s))