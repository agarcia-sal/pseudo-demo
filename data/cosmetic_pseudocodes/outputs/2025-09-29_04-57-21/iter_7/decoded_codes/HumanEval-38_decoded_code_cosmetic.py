from typing import List


def encode_cyclic(input_string: str) -> str:
    groups: List[str] = []
    max_index: int = ((len(input_string) + 2) // 3) - 1
    i: int = 0

    while i <= max_index:
        start_pos: int = i * 3
        end_pos: int = start_pos + 3
        if end_pos > len(input_string):
            end_pos = len(input_string)
        groups.append(input_string[start_pos:end_pos])
        i += 1

    rotated: List[str] = []
    for grp in groups:
        if len(grp) == 3:
            # rotate by moving first character to the end
            rotated_part = grp[1:3] + grp[0]
            rotated.append(rotated_part)
        else:
            rotated.append(grp)

    result: str = "".join(rotated)
    return result


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))