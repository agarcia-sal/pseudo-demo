from typing import List

def encode_cyclic(input_string: str) -> str:
    groups: List[str] = []
    length: int = len(input_string)
    number_of_groups: int = (length + 2) // 3  # Number of groups of up to 3 chars

    for i in range(number_of_groups):
        start_index: int = 3 * i
        end_index: int = min(start_index + 3, length)
        group: str = input_string[start_index:end_index]
        if len(group) == 3:
            # Rotate first character to the end
            group = group[1:] + group[0]
        groups.append(group)

    encoded_string: str = ''.join(groups)
    return encoded_string


def decode_cyclic(input_string: str) -> str:
    # Decoding is applying the same process twice
    return encode_cyclic(encode_cyclic(input_string))