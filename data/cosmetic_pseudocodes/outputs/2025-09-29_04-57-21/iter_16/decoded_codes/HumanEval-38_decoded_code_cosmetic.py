from typing import List


def encode_cyclic(input_string: str) -> str:
    segments: List[str] = []
    counter: int = 0
    total_groups: int = (len(input_string) + 2) // 3  # number of 3-char groups (ceil division)

    while counter < total_groups:
        start_pos: int = counter * 3
        end_pos: int = start_pos + 3
        if end_pos > len(input_string):
            end_pos = len(input_string)
        segments.append(input_string[start_pos:end_pos])
        counter += 1

    transformed_segments: List[str] = []
    for part in segments:
        if len(part) == 3:
            # rotate first char to the end
            rotated = part[1:] + part[0]
            transformed_segments.append(rotated)
        else:
            transformed_segments.append(part)

    return "".join(transformed_segments)


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))