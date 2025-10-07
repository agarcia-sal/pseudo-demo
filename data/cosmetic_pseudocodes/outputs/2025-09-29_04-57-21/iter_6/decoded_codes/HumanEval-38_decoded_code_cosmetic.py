from typing import List


def encode_cyclic(input_string: str) -> str:
    segments: List[str] = []
    count: int = (len(input_string) + 2) // 3
    for pos in range(count):
        start_pos = pos * 3
        end_pos = start_pos + 3
        if end_pos > len(input_string):
            end_pos = len(input_string)
        segments.append(input_string[start_pos:end_pos])

    transformed: List[str] = []
    for chunk in segments:
        if len(chunk) == 3:
            # Move the first character to the end
            transformed.append(chunk[1:] + chunk[0])
        else:
            transformed.append(chunk)
    return ''.join(transformed)


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))