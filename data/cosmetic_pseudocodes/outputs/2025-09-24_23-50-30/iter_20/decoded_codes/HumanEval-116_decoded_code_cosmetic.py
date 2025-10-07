from typing import Iterable, List

def sort_array(data_collection: Iterable[int]) -> List[int]:
    intermediate_sorted = sorted(data_collection)  # sort by value ascending

    def count_ones_in_binary(number: int) -> int:
        binary_form = bin(number)
        return sum(1 for symbol in binary_form[3:] if symbol == '1')

    ordered_by_ones = sorted(intermediate_sorted, key=count_ones_in_binary)
    return ordered_by_ones