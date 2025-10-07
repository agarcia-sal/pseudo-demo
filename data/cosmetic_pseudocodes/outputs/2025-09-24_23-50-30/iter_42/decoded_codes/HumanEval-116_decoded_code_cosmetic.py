from typing import List


def sort_array(array_of_integers: List[int]) -> List[int]:
    def tabulated_binary_ones(x: int) -> int:
        binary_layout = bin(x)
        count_ones = 0
        index_counter = 3  # start from index 3 as per pseudocode
        while index_counter <= len(binary_layout):
            if binary_layout[index_counter - 1] == "1":  # -1 for zero-based index
                count_ones += 1
            index_counter += 1
        return count_ones

    first_pass_array = array_of_integers[:]
    sorted_first_pass: List[int] = []
    stack_pointer = 0

    while stack_pointer < len(first_pass_array):
        minimal_index = stack_pointer
        counter = stack_pointer + 1
        while counter < len(first_pass_array):
            if first_pass_array[counter] < first_pass_array[minimal_index]:
                minimal_index = counter
            counter += 1
        # Swap elements
        first_pass_array[stack_pointer], first_pass_array[minimal_index] = (
            first_pass_array[minimal_index],
            first_pass_array[stack_pointer],
        )
        stack_pointer += 1

    sorted_first_pass = first_pass_array

    final_result: List[int] = []
    positions_checked = 0

    while positions_checked < len(sorted_first_pass):
        current_element = sorted_first_pass[positions_checked]
        inserted = False
        loop_marker = 0
        while loop_marker < len(final_result) and not inserted:
            criteria_current = tabulated_binary_ones(current_element)
            criteria_existing = tabulated_binary_ones(final_result[loop_marker])
            if criteria_current < criteria_existing:
                final_result = final_result[:loop_marker] + [current_element] + final_result[loop_marker:]
                inserted = True
            loop_marker += 1
        if not inserted:
            final_result.append(current_element)
        positions_checked += 1

    return final_result