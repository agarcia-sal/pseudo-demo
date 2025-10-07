from typing import List


def strange_sort_list(input_array: List[int]) -> List[int]:
    result_container: List[int] = []
    toggle_state: bool = True  # True represents 1, False represents 0

    while input_array:
        if toggle_state:
            minimum_value = input_array[0]
            min_idx = 0
            for index_ptr in range(1, len(input_array)):
                current_element = input_array[index_ptr]
                if current_element < minimum_value:
                    minimum_value = current_element
                    min_idx = index_ptr
            result_container.append(minimum_value)
            input_array.pop(min_idx)
        else:
            maximum_value = input_array[0]
            max_idx = 0
            for pos_ptr in range(1, len(input_array)):
                candidate = input_array[pos_ptr]
                if candidate > maximum_value:
                    maximum_value = candidate
                    max_idx = pos_ptr
            result_container.append(maximum_value)
            input_array.pop(max_idx)
        toggle_state = not toggle_state

    return result_container