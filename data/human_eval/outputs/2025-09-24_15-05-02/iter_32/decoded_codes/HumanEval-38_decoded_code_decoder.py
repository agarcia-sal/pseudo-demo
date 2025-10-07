from typing import List


def encode_cyclic(input_string: str) -> str:
    groups: List[str] = []
    n = (len(input_string) + 2) // 3
    for index in range(n):
        start_index = 3 * index
        end_index = min(3 * index + 3, len(input_string))
        groups.append(input_string[start_index:end_index])
    for i, group in enumerate(groups):
        if len(group) == 3:
            groups[i] = group[1:] + group[0]
    result_string = ''.join(groups)
    return result_string


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))