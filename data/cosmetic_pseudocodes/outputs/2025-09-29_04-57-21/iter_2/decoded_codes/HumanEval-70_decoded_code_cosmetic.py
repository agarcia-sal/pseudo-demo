from typing import List

def strange_sort_list(input_array: List[int]) -> List[int]:
    output_collection: List[int] = []
    toggle_switch: int = 1

    while input_array:
        if toggle_switch == 1:
            chosen_element = input_array[0]
            for item in input_array:
                if item < chosen_element:
                    chosen_element = item
        else:
            chosen_element = input_array[0]
            index_tracker = 0
            for index in range(len(input_array)):
                if input_array[index] > chosen_element:
                    chosen_element = input_array[index]
                    index_tracker = index

        output_collection.append(chosen_element)

        for pos in range(len(input_array)):
            if input_array[pos] == chosen_element:
                input_array.pop(pos)
                break

        toggle_switch = 1 - toggle_switch

    return output_collection