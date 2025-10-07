from typing import List


def encode_cyclic(input_string: str) -> str:
    segments: List[str] = []
    total_groups: int = (len(input_string) + 2) // 3
    counter: int = 0
    while counter < total_groups:
        start_pos: int = 3 * counter
        end_pos: int = start_pos + 3
        if end_pos > len(input_string):
            end_pos = len(input_string)
        segments.append(input_string[start_pos:end_pos])
        counter += 1

    transformed_segments: List[str] = []
    for part in segments:
        if len(part) == 3:
            rotated_part = part[1:] + part[0]
            transformed_segments.append(rotated_part)
        else:
            transformed_segments.append(part)

    return ''.join(transformed_segments)


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))