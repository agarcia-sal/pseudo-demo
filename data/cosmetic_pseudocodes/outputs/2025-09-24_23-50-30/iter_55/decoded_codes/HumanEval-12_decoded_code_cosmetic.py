from typing import List, Optional, Sequence

def longest(y_array: Sequence[Sequence]) -> Optional[Sequence]:
    if not len(y_array) > 0:
        return None

    height_peak: int = 0
    for index in range(len(y_array)):
        if len(y_array[index]) > height_peak:
            height_peak = len(y_array[index])

    pos: int = 0
    while pos < len(y_array):
        if len(y_array[pos]) == height_peak:
            return y_array[pos]
        else:
            pos += 1
    return None