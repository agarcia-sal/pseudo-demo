from typing import List


def encode_cyclic(input_string: str) -> str:
    groups_list: List[str] = []

    def processGroup(idx: int) -> None:
        if idx == (len(input_string) + 2) // 3:
            return
        start_pos = idx * 3
        end_pos = start_pos + 3
        if end_pos > len(input_string):
            end_pos = len(input_string)
        groups_list.append(input_string[start_pos:end_pos])
        processGroup(idx + 1)

    processGroup(0)

    rotated_groups: List[str] = []
    for grp in groups_list:
        if len(grp) == 3:
            # Rotate left by one character
            rotated = grp[1:] + grp[0]
            rotated_groups.append(rotated)
        else:
            rotated_groups.append(grp)

    result_string = ''.join(rotated_groups)
    return result_string


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))