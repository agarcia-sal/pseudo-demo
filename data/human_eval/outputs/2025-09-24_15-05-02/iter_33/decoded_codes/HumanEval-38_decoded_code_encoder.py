from typing import List

def encode_cyclic(string_input: str) -> str:
    groups: List[str] = []
    n = len(string_input)
    # number of groups is ceil(n/3), implemented as integer division with adjustment
    num_groups = (n + 2) // 3
    for index in range(num_groups):
        start = 3 * index
        end = min(start + 3, n)
        group = string_input[start:end]
        if len(group) == 3:
            group = group[1:] + group[0]
        groups.append(group)
    encoded_string = ''.join(groups)
    return encoded_string

def decode_cyclic(string_input: str) -> str:
    return encode_cyclic(encode_cyclic(string_input))