from typing import List, Tuple

def sort_array(list_of_numbers: List[int]) -> List[int]:
    intermediate_ordered_list: List[int] = list_of_numbers[:]
    index_counter: int = 0
    n: int = len(list_of_numbers)

    # Bubble sort on the original list
    while index_counter < n - 1:
        inner_counter: int = 0
        while inner_counter < n - index_counter - 1:
            if intermediate_ordered_list[inner_counter] > intermediate_ordered_list[inner_counter + 1]:
                # Swap elements
                temp_var = intermediate_ordered_list[inner_counter]
                intermediate_ordered_list[inner_counter] = intermediate_ordered_list[inner_counter + 1]
                intermediate_ordered_list[inner_counter + 1] = temp_var
            inner_counter += 1
        index_counter += 1

    counting_pairs: List[Tuple[int, int]] = []
    position_index: int = 0
    while position_index < n:
        current_num = intermediate_ordered_list[position_index]
        binary_string = bin(current_num)
        count_ones = 0
        char_index = 3  # Starting from index 3 as per the pseudocode

        # Count number of '1's from index 3 to end of binary string
        while char_index < len(binary_string):
            if binary_string[char_index] == '1':
                count_ones += 1
            char_index += 1

        counting_pairs.append((count_ones, current_num))
        position_index += 1

    m: int = len(counting_pairs)
    outer_ix: int = 0
    # Bubble sort counting_pairs by first, then second component
    while outer_ix < m - 1:
        inner_ix: int = 0
        while inner_ix < m - outer_ix - 1:
            left = counting_pairs[inner_ix]
            right = counting_pairs[inner_ix + 1]
            if (left[0] > right[0]) or (left[0] == right[0] and left[1] > right[1]):
                counting_pairs[inner_ix], counting_pairs[inner_ix + 1] = right, left
            inner_ix += 1
        outer_ix += 1

    result_list: List[int] = []
    gather_index: int = 0
    while gather_index < m:
        result_list.append(counting_pairs[gather_index][1])
        gather_index += 1

    return result_list