from typing import List

def sort_array(numbers_list: List[int]) -> List[int]:
    temp_sorted_list = sorted(numbers_list)

    count_ones_key: List[int] = []
    for current_element in temp_sorted_list:
        binary_form = bin(current_element)
        binary_substring = binary_form[2:]  # Remove '0b' prefix
        ones_count = sum(ch == '1' for ch in binary_substring)
        count_ones_key.append(ones_count)

    zipped_pairs = list(zip(count_ones_key, temp_sorted_list))
    sorted_pairs = sorted(zipped_pairs, key=lambda pair: pair[0])

    final_array: List[int] = [pair[1] for pair in sorted_pairs]
    return final_array