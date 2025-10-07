from typing import Sequence, Optional, Tuple

def find_closest_elements(sequence_data: Sequence[int]) -> Optional[Tuple[int, int]]:
    minimum_separation: Optional[int] = None
    result_pair: Optional[Tuple[int, int]] = None
    index_a: int = 0
    length: int = len(sequence_data)

    while index_a < length:
        value_a = sequence_data[index_a]
        index_b = 0
        while index_b < length:
            value_b = sequence_data[index_b]
            if index_a != index_b:
                difference = abs(value_a - value_b)
                if minimum_separation is None:
                    result_pair = tuple(sorted((value_a, value_b)))
                    minimum_separation = difference
                else:
                    if difference < minimum_separation:
                        minimum_separation = difference
                        result_pair = tuple(sorted((value_a, value_b)))
            index_b += 1
        index_a += 1
    return result_pair