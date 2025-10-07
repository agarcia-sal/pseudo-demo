from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    def recursive_median(sorted_seq: List[Union[int, float]], idx: int) -> float:
        if idx == 0:
            return (sorted_seq[0] + sorted_seq[1]) / 2.0
        elif idx == 1:
            mid_index = (len(sorted_seq) - 1) // 2
            return sorted_seq[mid_index]

    elements_sorted: List[Union[int, float]] = []
    for elem in list_of_elements:
        elements_sorted = elements_sorted + [elem]
    elements_sorted.sort()

    count_elements = len(elements_sorted)
    if count_elements % 2 != 0:
        return recursive_median(elements_sorted, 1)
    else:
        mid_low_index = (count_elements // 2) - 1
        mid_high_index = count_elements // 2
        first_mid = elements_sorted[mid_low_index]
        second_mid = elements_sorted[mid_high_index]
        return (first_mid + second_mid) * 0.5