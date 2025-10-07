from typing import List


def encode_cyclic(input_string: str) -> str:
    segments: List[str] = []
    total_groups: int = (len(input_string) + 2) // 3
    idx: int = 0
    while idx < total_groups:
        start_pos: int = idx * 3
        end_pos: int = min(start_pos + 3, len(input_string))
        segments.append(input_string[start_pos:end_pos])
        idx += 1

    transformed: List[str] = []
    for segment in segments:
        if len(segment) == 3:
            rotated: str = segment[1:] + segment[0]
            transformed.append(rotated)
        else:
            transformed.append(segment)

    return "".join(transformed)


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))