from typing import List

def encode_cyclic(input_string: str) -> str:
    groups: List[str] = []
    total_groups: int = (len(input_string) + 2) // 3
    for i in range(total_groups):
        start_pos = 3 * i
        end_pos = min(start_pos + 3, len(input_string))
        groups.append(input_string[start_pos:end_pos])

    result: List[str] = []
    for chunk in groups:
        if len(chunk) == 3:
            # chunk[2:] is the third character, chunk[1] is the second character
            result.append(chunk[2] + chunk[1])
        else:
            result.append(chunk)
    return ''.join(result)


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))