from typing import List, TypeVar

T = TypeVar('T')

def strange_sort_list(unordered_values: List[T]) -> List[T]:
    ordered_collection: List[T] = []
    toggle_indicator: bool = True

    while unordered_values:
        if toggle_indicator:
            chosen_element: T = unordered_values[0]
            iterator_i: int = 1
            while iterator_i < len(unordered_values):
                if unordered_values[iterator_i] < chosen_element:
                    chosen_element = unordered_values[iterator_i]
                iterator_i += 1
            ordered_collection.append(chosen_element)
        else:
            chosen_element = unordered_values[0]
            iterator_j: int = 1
            while iterator_j < len(unordered_values):
                if unordered_values[iterator_j] > chosen_element:
                    chosen_element = unordered_values[iterator_j]
                iterator_j += 1
            ordered_collection.append(chosen_element)

        removal_index: int = -1
        search_index: int = 0
        last_added = ordered_collection[-1]
        while search_index < len(unordered_values):
            if unordered_values[search_index] == last_added:
                removal_index = search_index
                break
            search_index += 1

        if removal_index != -1:
            unordered_values.pop(removal_index)

        toggle_indicator = not toggle_indicator

    return ordered_collection