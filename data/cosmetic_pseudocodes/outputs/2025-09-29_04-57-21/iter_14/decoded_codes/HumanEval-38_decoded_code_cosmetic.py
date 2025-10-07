from typing import List


def encode_cyclic(input_string: str) -> str:
    segments: List[str] = []
    position: int = 0
    length: int = len(input_string)
    while position < length:
        end_bound = position + 3
        if end_bound > length:
            end_bound = length
        segments.append(input_string[position:end_bound])
        position += 3

    transformed_segments: List[str] = []
    segment_ptr: int = 0
    while segment_ptr < len(segments):
        current_segment = segments[segment_ptr]
        if len(current_segment) == 3:
            # move first char to the end of the segment
            rearranged = current_segment[1:] + current_segment[0]
            transformed_segments.append(rearranged)
        else:
            transformed_segments.append(current_segment)
        segment_ptr += 1

    result_string = ''.join(transformed_segments)
    return result_string


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))