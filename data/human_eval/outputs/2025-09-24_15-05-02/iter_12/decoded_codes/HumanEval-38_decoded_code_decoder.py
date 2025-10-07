from typing import List

def encode_cyclic(input_string: str) -> str:
    group_count = (len(input_string) + 2) // 3
    groups: List[str] = []
    for i in range(group_count):
        start_index = 3 * i
        end_index = min(3 * i + 3, len(input_string))
        groups.append(input_string[start_index:end_index])
    for i in range(len(groups)):
        if len(groups[i]) == 3:
            group = groups[i]
            groups[i] = group[1:] + group[0]
    encoded_string = "".join(groups)
    return encoded_string

def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))