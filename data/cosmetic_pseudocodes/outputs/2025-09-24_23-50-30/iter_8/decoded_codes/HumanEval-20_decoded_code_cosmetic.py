from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    result_pair: Optional[Tuple[int, int]] = None
    smallest_gap: Optional[int] = None

    for posX in range(len(list_of_numbers)):
        valX = list_of_numbers[posX]
        for posY in range(len(list_of_numbers)):
            if posY != posX:
                gap = abs(valX - list_of_numbers[posY])
                if smallest_gap is None or gap < smallest_gap:
                    smallest_gap = gap
                    valY = list_of_numbers[posY]
                    # Ensure the smaller value is first in the tuple
                    if valX < valY:
                        result_pair = (valX, valY)
                    else:
                        result_pair = (valY, valX)

    return result_pair