from typing import List, Dict


def sort_array(numbers_list: List[int]) -> List[int]:
    def count_ones(binary_string: str) -> int:
        return sum(1 for ch in binary_string if ch == '1')

    length_numbers = len(numbers_list)
    # Sort numbers_list in-place using a simple selection sort logic
    for i in range(length_numbers - 1):
        for j in range(i + 1, length_numbers):
            if numbers_list[i] > numbers_list[j]:
                numbers_list[i], numbers_list[j] = numbers_list[j], numbers_list[i]

    temp_sorted = numbers_list

    dict_groups: Dict[int, List[int]] = {}
    for each_value in temp_sorted:
        binary_str = bin(each_value)
        binary_rep = binary_str[2:]  # substring excluding '0b'
        key_count = count_ones(binary_rep)
        if key_count not in dict_groups:
            dict_groups[key_count] = []
        dict_groups[key_count].append(each_value)

    result_sorted: List[int] = []
    for each_key in sorted(dict_groups.keys()):
        result_sorted += dict_groups[each_key]

    return result_sorted