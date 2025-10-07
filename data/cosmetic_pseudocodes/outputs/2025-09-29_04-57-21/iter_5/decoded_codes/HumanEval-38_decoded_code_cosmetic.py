from typing import List


def encode_cyclic(input_string: str) -> str:
    segment_collection: List[str] = []
    limit: int = (len(input_string) + 2) // 3  # number of 3-char segments, rounding up
    idx: int = 0
    while idx < limit:
        start_pos = idx * 3
        end_pos = start_pos + 3
        if end_pos > len(input_string):
            end_pos = len(input_string)
        segment_collection.append(input_string[start_pos:end_pos])
        idx += 1

    transformed_segments: List[str] = []
    for segment in segment_collection:
        if len(segment) != 3:
            transformed_segments.append(segment)
            continue
        tail_part = segment[1:3]
        head_char = segment[0]
        transformed_segments.append(tail_part + head_char)

    result_string = "".join(transformed_segments)
    return result_string


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))