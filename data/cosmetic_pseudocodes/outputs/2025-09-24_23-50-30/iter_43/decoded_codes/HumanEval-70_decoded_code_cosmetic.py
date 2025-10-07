from typing import List

def strange_sort_list(array_of_numbers: List[int]) -> List[int]:
    output_collection: List[int] = []
    toggle_switch: int = 1
    while array_of_numbers:
        if toggle_switch == 1:
            selected_element = min(array_of_numbers)
        else:
            selected_element = max(array_of_numbers)
        output_collection.append(selected_element)
        for index, value in enumerate(array_of_numbers):
            if value == selected_element:
                del array_of_numbers[index]
                break
        toggle_switch = (toggle_switch + 1) % 2
    return output_collection