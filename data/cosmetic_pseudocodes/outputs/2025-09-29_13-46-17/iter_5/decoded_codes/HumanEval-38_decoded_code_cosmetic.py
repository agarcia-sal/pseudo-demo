from typing import List


def encode_cyclic(input_string: str) -> str:
    slice_list: List[str] = []
    max_i: int = (len(input_string) + 2) // 3 - 1
    current: int = 0
    while current <= max_i:
        start_pos: int = 3 * current
        end_pos: int = start_pos + 3
        if end_pos > len(input_string):
            end_pos = len(input_string)
        slice_list.append(input_string[start_pos:end_pos])
        current += 1

    transformed: List[str] = []
    for segment in slice_list:
        if len(segment) == 3:
            rotated = segment[1:] + segment[0]
            transformed.append(rotated)
        else:
            transformed.append(segment)

    result_str: str = "".join(transformed)
    return result_str


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))