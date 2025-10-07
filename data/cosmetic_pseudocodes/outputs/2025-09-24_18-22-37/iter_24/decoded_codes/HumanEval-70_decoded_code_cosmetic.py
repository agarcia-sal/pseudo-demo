from typing import List


def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    accumulation_array: List[int] = []
    toggle_indicator: bool = True
    while list_of_integers:
        if toggle_indicator:
            smallest_element = list_of_integers[0]
            temp_index = 0
            for iterator_index in range(len(list_of_integers)):
                if list_of_integers[iterator_index] < smallest_element:
                    smallest_element = list_of_integers[iterator_index]
                    temp_index = iterator_index
            accumulation_array.append(smallest_element)
            list_of_integers.pop(temp_index)
        else:
            largest_element = list_of_integers[0]
            temp_pos = 0
            for iterator_pos in range(len(list_of_integers)):
                if list_of_integers[iterator_pos] > largest_element:
                    largest_element = list_of_integers[iterator_pos]
                    temp_pos = iterator_pos
            accumulation_array.append(largest_element)
            list_of_integers.pop(temp_pos)
        toggle_indicator = not toggle_indicator
    return accumulation_array