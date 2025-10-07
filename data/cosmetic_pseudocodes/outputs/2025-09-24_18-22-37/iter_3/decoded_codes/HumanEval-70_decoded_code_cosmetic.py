from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    output_sequence: List[int] = []
    toggle_selection: bool = False
    input_list = list_of_integers[:]  # Make a copy to avoid modifying the original list
    while input_list:
        if not toggle_selection:
            chosen_element = input_list[0]
            for element in input_list:
                if element < chosen_element:
                    chosen_element = element
        else:
            chosen_element = input_list[0]
            for element in input_list:
                if element > chosen_element:
                    chosen_element = element
        output_sequence.append(chosen_element)
        input_list.remove(chosen_element)
        toggle_selection = not toggle_selection
    return output_sequence