from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    output_sequence: List[int] = []
    toggle_indicator: bool = False
    while list_of_integers:
        if not toggle_indicator:
            smallest_element: int = list_of_integers[0]
            for index in range(1, len(list_of_integers)):
                if list_of_integers[index] < smallest_element:
                    smallest_element = list_of_integers[index]
            chosen_element = smallest_element
        else:
            largest_element: int = list_of_integers[0]
            for index in range(1, len(list_of_integers)):
                if list_of_integers[index] > largest_element:
                    largest_element = list_of_integers[index]
            chosen_element = largest_element

        output_sequence.append(chosen_element)

        list_of_integers = [each_element for each_element in list_of_integers if each_element != chosen_element]

        toggle_indicator = not toggle_indicator
    return output_sequence