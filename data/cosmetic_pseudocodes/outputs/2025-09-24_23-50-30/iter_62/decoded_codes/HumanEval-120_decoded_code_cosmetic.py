from typing import List

def maximum(list_of_numbers: List[int], count_positive: int) -> List[int]:
    def extract_tail(data: List[int], count: int, length_accum: int) -> List[int]:
        if count == 0:
            return []
        else:
            # recurse on tail (excluding first element), decrement count, increment length_accum
            return extract_tail(data[1:], count - 1, length_accum + 1) + [data[0]]

    if count_positive == 0:
        return []

    sorted_list = sorted(list_of_numbers)
    total_length = len(sorted_list)  # although total_length unused, preserved as in pseudocode
    return extract_tail(sorted_list, count_positive, 0)