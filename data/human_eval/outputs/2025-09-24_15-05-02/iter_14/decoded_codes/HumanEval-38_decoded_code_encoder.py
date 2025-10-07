from typing import List

def encode_cyclic(string_input: str) -> str:
    number_of_groups = (len(string_input) + 2) // 3
    groups: List[str] = []
    for index in range(number_of_groups):
        start_index = 3 * index
        end_index = min(3 * index + 3, len(string_input))
        groups.append(string_input[start_index:end_index])
    cycled_groups: List[str] = []
    for group in groups:
        if len(group) == 3:
            cycled_groups.append(group[1:] + group[0])
        else:
            cycled_groups.append(group)
    encoded_string = ''.join(cycled_groups)
    return encoded_string

def decode_cyclic(string_input: str) -> str:
    return encode_cyclic(encode_cyclic(string_input))