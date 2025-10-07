from typing import List

def encode_cyclic(input_string: str) -> str:
    groups: List[str] = []
    length: int = len(input_string)
    number_of_groups: int = (length + 2) // 3
    for i in range(number_of_groups):
        start_index: int = 3 * i
        end_index: int = min(start_index + 3, length)
        group: str = input_string[start_index:end_index]
        if len(group) == 3:
            group = group[1:] + group[0]
        groups.append(group)
    return "".join(groups)

def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))