from typing import List


def encode_cyclic(input_string: str) -> str:
    segments: List[str] = []
    total_segments: int = (len(input_string) + 2) // 3  # ceil division for chunks of size 3
    counter: int = 0
    while counter < total_segments:
        start_pos = counter * 3
        end_pos = start_pos + 3
        if end_pos > len(input_string):
            end_pos = len(input_string)
        segments.append(input_string[start_pos:end_pos])
        counter += 1

    transformed_segments: List[str] = []
    for segment in segments:
        if len(segment) == 3:
            rearranged = segment[1:3] + segment[0]
            transformed_segments.append(rearranged)
        else:
            transformed_segments.append(segment)

    return "".join(transformed_segments)


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))