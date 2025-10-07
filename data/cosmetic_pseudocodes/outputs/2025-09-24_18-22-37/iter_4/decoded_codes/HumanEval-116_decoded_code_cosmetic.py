from typing import List, Dict


def sort_array(array_of_integers: List[int]) -> List[int]:
    temp_sorted_list: List[int] = array_of_integers[:]
    index: int = 0
    length = len(temp_sorted_list)
    while index < length - 1:
        swap_occurred: bool = False
        j: int = 0
        while j < length - 1 - index:
            if temp_sorted_list[j] > temp_sorted_list[j + 1]:
                tmp = temp_sorted_list[j]
                temp_sorted_list[j] = temp_sorted_list[j + 1]
                temp_sorted_list[j + 1] = tmp
                swap_occurred = True
            j += 1
        if not swap_occurred:
            break
        index += 1

    buckets: Dict[int, List[int]] = {}
    k: int = 0
    while k < length:
        binary_form = bin(temp_sorted_list[k])[2:]
        count_ones: int = 0
        m: int = 0
        while m < len(binary_form):
            if binary_form[m] == '1':
                count_ones += 1
            m += 1
        if count_ones not in buckets:
            buckets[count_ones] = []
        buckets[count_ones].append(temp_sorted_list[k])
        k += 1

    sorted_keys = list(buckets.keys())
    sorted_keys_list: List[int] = []
    for key in sorted_keys:
        sorted_keys_list.append(key)

    p: int = 0
    length_keys = len(sorted_keys_list)
    while p < length_keys - 1:
        swapped: bool = False
        q: int = 0
        while q < length_keys - 1 - p:
            if sorted_keys_list[q] > sorted_keys_list[q + 1]:
                tmp_key = sorted_keys_list[q]
                sorted_keys_list[q] = sorted_keys_list[q + 1]
                sorted_keys_list[q + 1] = tmp_key
                swapped = True
            q += 1
        if not swapped:
            break
        p += 1

    result_array: List[int] = []
    r: int = 0
    while r < len(sorted_keys_list):
        current_key = sorted_keys_list[r]
        val_list = buckets[current_key]
        s: int = 0
        while s < len(val_list):
            result_array.append(val_list[s])
            s += 1
        r += 1

    return result_array