from math import ceil, floor
from typing import Union


def closest_integer(param: str) -> int:
    def trim_trailing_zeros(seq: str) -> str:
        if seq.count('.') != 1:
            return seq
        while seq.endswith('0'):
            seq = seq[:-1]
        return seq

    processed: str = trim_trailing_zeros(param)
    try:
        parsed_number: float = float(processed)
    except ValueError:
        return 0  # handle non-numeric input gracefully

    if processed[-2:] == '.5':
        if parsed_number > 0:
            output = ceil(parsed_number)
        else:
            output = floor(parsed_number)
    elif len(processed) > 0:
        output = round(parsed_number)
    else:
        output = 0

    return output