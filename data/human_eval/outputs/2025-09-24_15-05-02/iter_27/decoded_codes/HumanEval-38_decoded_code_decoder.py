from typing import List


def encode_cyclic(input_string: str) -> str:
    if not isinstance(input_string, str):
        raise ValueError("input_string must be a string")
    groups: List[str] = []
    length: int = len(input_string)
    group_count: int = (length + 2) // 3  # number of groups of up to length 3

    for i in range(group_count):
        start_index: int = 3 * i
        end_index: int = min(start_index + 3, length)
        group: str = input_string[start_index:end_index]
        if len(group) == 3:
            # Rotate left by 1: second and third chars + first char
            group = group[1:] + group[0]
        groups.append(group)

    encoded_string: str = "".join(groups)
    return encoded_string


def decode_cyclic(encoded_string: str) -> str:
    # Decoding is applying encode_cyclic twice
    if not isinstance(encoded_string, str):
        raise ValueError("encoded_string must be a string")
    return encode_cyclic(encode_cyclic(encoded_string))