from typing import Sequence, List

def sort_array(sequence_of_numbers: Sequence[int]) -> List[int]:
    ascending_ordered_list: List[int] = sorted(sequence_of_numbers)
    # Sort by number of '1's in binary representation, stable with ascending order as tiebreaker
    sorted_by_bitcount: List[int] = sorted(ascending_ordered_list, key=lambda number_param: bin(number_param).count('1'))
    return sorted_by_bitcount