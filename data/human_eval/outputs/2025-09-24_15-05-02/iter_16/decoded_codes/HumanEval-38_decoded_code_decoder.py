from typing import List


def encode_cyclic(input_string: str) -> str:
    groups: List[str] = []
    length: int = len(input_string)
    group_count: int = (length + 2) // 3  # Integer division
    for i in range(group_count):
        start_index = 3 * i
        end_index = min(3 * i + 3, length)
        group = input_string[start_index:end_index]
        groups.append(group)
    for idx, group in enumerate(groups):
        if len(group) == 3:
            groups[idx] = group[1:] + group[0]  # Rotate left by one character
    encoded_string = ''.join(groups)
    return encoded_string


def decode_cyclic(encoded_string: str) -> str:
    return encode_cyclic(encode_cyclic(encoded_string))