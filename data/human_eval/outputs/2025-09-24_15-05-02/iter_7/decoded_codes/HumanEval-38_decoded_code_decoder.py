from typing import List

def encode_cyclic(input_string: str) -> str:
    groups: List[str] = []
    number_of_groups = (len(input_string) + 2) // 3
    for i in range(number_of_groups):
        start_index = 3 * i
        end_index = min(3 * i + 3, len(input_string))
        group = input_string[start_index:end_index]
        if len(group) == 3:
            group = group[1:] + group[0]
        groups.append(group)
    return "".join(groups)

def decode_cyclic(encoded_string: str) -> str:
    return encode_cyclic(encode_cyclic(encoded_string))