from typing import List

def encode_cyclic(input_string: str) -> str:
    groups: List[str] = []
    length = len(input_string)
    for index in range((length + 2) // 3):
        start_pos = 3 * index
        end_pos = min(3 * index + 3, length)
        groups.append(input_string[start_pos:end_pos])

    for i in range(len(groups)):
        group = groups[i]
        if len(group) == 3:
            groups[i] = group[1:] + group[0]

    return ''.join(groups)

def decode_cyclic(encoded_string: str) -> str:
    return encode_cyclic(encode_cyclic(encoded_string))