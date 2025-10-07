from typing import List


def encode_cyclic(input_string: str) -> str:
    segments: List[str] = []
    counter: int = 0
    length: int = len(input_string)
    while counter * 3 < length:
        start_index: int = counter * 3
        end_index: int = start_index + 3
        if end_index > length:
            end_index = length
        segments.append(input_string[start_index:end_index])
        counter += 1

    transformed_segments: List[str] = []
    for segment in segments:
        if len(segment) != 3:
            transformed_segments.append(segment)
            continue
        # Rearrange: third char + second char + first char of the segment
        rearranged = segment[2:3] + segment[1:2] + segment[0:1]
        transformed_segments.append(rearranged)
    return "".join(transformed_segments)


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))