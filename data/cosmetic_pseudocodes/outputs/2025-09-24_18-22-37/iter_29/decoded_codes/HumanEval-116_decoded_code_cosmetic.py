from typing import Iterable, List

def sort_array(numerical_collection: Iterable[int]) -> List[int]:
    intermediate_list: List[int] = sorted(numerical_collection)
    # Sort by number of set bits in ascending order
    final_list_to_return: List[int] = sorted(intermediate_list, key=lambda x: bin(x)[2:].count('1'))
    return final_list_to_return