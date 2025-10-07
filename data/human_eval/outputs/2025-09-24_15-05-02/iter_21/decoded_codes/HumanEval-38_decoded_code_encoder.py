from typing import List

def encode_cyclic(string: str) -> str:
    number_of_groups: int = (len(string) + 2) // 3
    groups: List[str] = []

    for index in range(number_of_groups):
        start: int = 3 * index
        end: int = min(start + 3, len(string))
        groups.append(string[start:end])

    for i, group in enumerate(groups):
        if len(group) == 3:
            groups[i] = group[1:] + group[0]

    encoded_string: str = "".join(groups)
    return encoded_string

def decode_cyclic(string: str) -> str:
    return encode_cyclic(encode_cyclic(string))