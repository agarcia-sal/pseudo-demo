from typing import List


def sort_array(array_of_integers: List[int]) -> List[int]:
    temp_sorted_list: List[int] = sorted(array_of_integers)

    def count_ones(bin_str: str) -> int:
        counter: int = 0
        idx: int = 0
        while idx < len(bin_str):
            if bin_str[idx] == '1':
                counter += 1
            idx += 1
        return counter

    result_list: List[int] = []
    i: int = 0
    while True:
        if i >= len(temp_sorted_list):
            break
        result_list.append(temp_sorted_list[i])
        i += 1

    result_list.sort(key=lambda element: count_ones(bin(element)[2:]))
    return result_list