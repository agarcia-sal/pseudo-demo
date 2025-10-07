from typing import Iterable, List


def sort_array(collection_of_values: Iterable[int]) -> List[int]:
    first_stage_sorted: List[int] = sorted(collection_of_values)
    # Sort by number of '1's in binary representation, ascending
    ultimate_result: List[int] = sorted(first_stage_sorted, key=lambda x: bin(x).count('1'))
    return ultimate_result