from typing import List


def encode_cyclic(input_string: str) -> str:
    segment_collection: List[str] = []
    total_segments: int = (len(input_string) + 2) // 3
    counter: int = 0

    while counter < total_segments:
        start_pos = 3 * counter
        end_pos = start_pos + 3
        if end_pos > len(input_string):
            end_pos = len(input_string)
        segment_collection.append(input_string[start_pos:end_pos])
        counter += 1

    transformed_segments: List[str] = []
    for segment in segment_collection:
        if len(segment) == 3:
            # rotate: move first char to the end
            rotated_segment = segment[1:3] + segment[0]
            transformed_segments.append(rotated_segment)
        else:
            transformed_segments.append(segment)

    return ''.join(transformed_segments)


def decode_cyclic(input_string: str) -> str:
    first_pass = encode_cyclic(input_string)
    return encode_cyclic(first_pass)