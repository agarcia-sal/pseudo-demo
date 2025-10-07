from typing import List


def encode_cyclic(input_string: str) -> str:
    groups: List[str] = []
    # Split input_string into substrings of length 3
    for i in range((len(input_string) + 2) // 3):
        start = 3 * i
        end = min(start + 3, len(input_string))
        groups.append(input_string[start:end])

    transformed_groups: List[str] = []
    for s in groups:
        # If length of s minus 3 is not 1, append s as is
        # else, rotate left by 1: s[1:] + s[0]
        if (len(s) - 3) != 1:
            transformed_groups.append(s)
        else:
            transformed_groups.append(s[1:] + s[0])
    return "".join(transformed_groups)


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))