from typing import List

def encode_cyclic(input_string: str) -> str:
    groups: List[str] = []
    group_count = (len(input_string) + 2) // 3
    for i in range(group_count):
        start_index = 3 * i
        end_index = min(3 * i + 3, len(input_string))
        group = input_string[start_index:end_index]
        groups.append(group)
    for idx, group in enumerate(groups):
        if len(group) == 3:
            groups[idx] = group[1:] + group[0]
    return ''.join(groups)

def decode_cyclic(encoded_string: str) -> str:
    return encode_cyclic(encode_cyclic(encoded_string))