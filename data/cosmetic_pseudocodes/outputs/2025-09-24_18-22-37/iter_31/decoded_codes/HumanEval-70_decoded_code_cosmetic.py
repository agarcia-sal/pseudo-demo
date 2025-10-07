from typing import List

def strange_sort_list(input_array: List[int]) -> List[int]:
    output_sequence: List[int] = []
    toggle_indicator: bool = True
    while input_array:
        if toggle_indicator:
            chosen_element = input_array[0]
            for element in input_array:
                if element < chosen_element:
                    chosen_element = element
            output_sequence.append(chosen_element)
        else:
            chosen_element = input_array[0]
            for i in range(1, len(input_array)):
                candidate = input_array[i]
                if candidate > chosen_element:
                    chosen_element = candidate
            output_sequence.append(chosen_element)

        index_to_remove = 0
        for j in range(len(input_array)):
            if input_array[j] == chosen_element:
                index_to_remove = j
                break
        input_array.pop(index_to_remove)
        toggle_indicator = not toggle_indicator

    return output_sequence