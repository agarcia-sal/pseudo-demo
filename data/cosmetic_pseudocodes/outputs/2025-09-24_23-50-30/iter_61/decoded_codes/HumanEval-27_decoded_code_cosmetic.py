from typing import Callable


def flip_case(coded_sequence: str) -> str:
    def helper_transform(index: int, length: int, accumulator: str) -> str:
        if index >= length:
            return accumulator
        ascii_val = ord(coded_sequence[index])
        if 65 <= ascii_val <= 90:
            new_char = coded_sequence[index].lower()
            return helper_transform(index + 1, length, accumulator + new_char)
        if 97 <= ascii_val <= 122:
            new_char = coded_sequence[index].upper()
            return helper_transform(index + 1, length, accumulator + new_char)
        return helper_transform(index + 1, length, accumulator + coded_sequence[index])

    return helper_transform(0, len(coded_sequence), "")