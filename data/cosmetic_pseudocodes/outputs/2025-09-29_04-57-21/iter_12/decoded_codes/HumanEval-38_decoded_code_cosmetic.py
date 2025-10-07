from typing import List


def encode_cyclic(input_string: str) -> str:
    segments: List[str] = []
    total_segments = (len(input_string) + 2) // 3
    current_position = 0
    while current_position < total_segments:
        start_index = 3 * current_position
        end_index = start_index + 3
        if end_index > len(input_string):
            end_index = len(input_string)
        segments.append(input_string[start_index:end_index])
        current_position += 1

    transformed_segments: List[str] = []
    for segment in segments:
        if len(segment) == 3:
            # Rotate by moving first character to the end
            rotated_segment = segment[1:3] + segment[0]
            transformed_segments.append(rotated_segment)
        else:
            transformed_segments.append(segment)

    return ''.join(transformed_segments)


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))