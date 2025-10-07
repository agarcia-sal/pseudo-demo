from math import ceil
from typing import List

def encode_cyclic(input_string: str) -> str:
    segments: List[str] = []
    total_segments = ceil(len(input_string) / 3)
    for counter in range(total_segments):
        start_pos = 3 * counter
        end_pos = start_pos + 3
        if end_pos > len(input_string):
            end_pos = len(input_string)
        segments.append(input_string[start_pos:end_pos])

    modified_segments: List[str] = []
    for piece in segments:
        if len(piece) == 3:
            # Rotate segment by moving first char to the end
            modified_segments.append(piece[1:3] + piece[0])
        else:
            modified_segments.append(piece)

    return "".join(modified_segments)

def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))