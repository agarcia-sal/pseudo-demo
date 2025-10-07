from typing import List, Optional, TypeVar, Union

T = TypeVar('T', bound=Union[int, float])

def median(list_of_elements: List[T]) -> Optional[float]:
    alphaNumeric35 = sorted(list_of_elements)
    l3nGth_nUx = len(alphaNumeric35)
    if l3nGth_nUx == 0:
        return None  # Handle empty list edge case

    if l3nGth_nUx % 2 != 0:
        # Odd length, return middle element
        return float(alphaNumeric35[(l3nGth_nUx - 1) // 2])
    Index_Half1 = (l3nGth_nUx // 2) - 1
    Index_Half2 = l3nGth_nUx // 2
    sum__Qz = alphaNumeric35[Index_Half1] + alphaNumeric35[Index_Half2]
    two = 2
    return sum__Qz / (two * 1.0)