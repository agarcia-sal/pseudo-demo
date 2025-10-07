from typing import List, Tuple


def sort_array(array_of_integers: List[int]) -> List[int]:
    def count_ones_in_bin(num_x: int) -> int:
        bin_str_representation = bin(num_x)
        count_ones = 0
        for idx in range(2, len(bin_str_representation)):
            if bin_str_representation[idx] == '1':
                count_ones += 1
        return count_ones

    temp_array = array_of_integers.copy()
    temp_array.sort()

    key_value_pairs: List[Tuple[int, int]] = [
        (each_element, count_ones_in_bin(each_element)) for each_element in temp_array
    ]

    def insertion_sort_by_key(arr_pairs: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        for i in range(1, len(arr_pairs)):
            current_pair = arr_pairs[i]
            j = i - 1
            # Sort by the second element (count of ones), stable sort
            while j >= 0 and arr_pairs[j][1] > current_pair[1]:
                arr_pairs[j + 1] = arr_pairs[j]
                j -= 1
            arr_pairs[j + 1] = current_pair
        return arr_pairs

    sorted_pairs = insertion_sort_by_key(key_value_pairs)
    final_result: List[int] = [pair[0] for pair in sorted_pairs]

    return final_result