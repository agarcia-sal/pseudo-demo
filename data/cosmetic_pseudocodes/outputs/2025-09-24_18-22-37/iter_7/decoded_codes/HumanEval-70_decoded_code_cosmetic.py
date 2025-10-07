from typing import List, TypeVar

T = TypeVar('T')

def strange_sort_list(elements_collection: List[T]) -> List[T]:
    output_array: List[T] = []
    toggle_indicator: bool = True
    while elements_collection:
        if toggle_indicator:
            chosen_element = elements_collection[0]
            for elem in elements_collection[1:]:
                if elem < chosen_element:
                    chosen_element = elem
            output_array.append(chosen_element)
        else:
            chosen_element = elements_collection[0]
            for elem in elements_collection[1:]:
                if elem > chosen_element:
                    chosen_element = elem
            output_array.append(chosen_element)
        removal_index = 0
        while removal_index < len(elements_collection):
            if elements_collection[removal_index] == chosen_element:
                break
            removal_index += 1
        elements_collection.pop(removal_index)
        toggle_indicator = not toggle_indicator
    return output_array