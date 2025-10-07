from typing import List, Dict


def sort_array(array_of_integers: List[int]) -> List[int]:
    temp_sorted_list: List[int] = []
    index_counter: int = 0
    while index_counter < len(array_of_integers):
        temp_sorted_list.append(array_of_integers[index_counter])
        index_counter += 1
    temp_sorted_list.sort()

    sort_key_dict: Dict[int, int] = {}
    element_cursor: int = 0
    while element_cursor < len(temp_sorted_list):
        current_elem: int = temp_sorted_list[element_cursor]
        bin_representation: str = bin(current_elem)
        bin_without_prefix: str = bin_representation[2:]  # strip '0b'
        count_ones: int = 0
        char_index: int = 0
        while char_index < len(bin_without_prefix):
            if bin_without_prefix[char_index] == '1':
                count_ones += 1
            char_index += 1
        sort_key_dict[current_elem] = count_ones
        element_cursor += 1

    final_result: List[int] = temp_sorted_list.copy()
    outer_idx: int = 0
    while outer_idx < len(final_result) - 1:
        inner_idx: int = outer_idx + 1
        while inner_idx < len(final_result):
            if sort_key_dict[final_result[outer_idx]] > sort_key_dict[final_result[inner_idx]]:
                temporary_holder: int = final_result[outer_idx]
                final_result[outer_idx] = final_result[inner_idx]
                final_result[inner_idx] = temporary_holder
            inner_idx += 1
        outer_idx += 1

    return final_result