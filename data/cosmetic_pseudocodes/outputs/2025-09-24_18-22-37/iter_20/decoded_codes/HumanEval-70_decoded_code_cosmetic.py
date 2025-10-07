from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    output_sequence: List[int] = []
    toggle_indicator: bool = True

    while list_of_integers:
        if toggle_indicator:
            smallest_element = list_of_integers[0]
            index_tracker = 0
            iterator_var = 1
            while iterator_var < len(list_of_integers):
                if list_of_integers[iterator_var] < smallest_element:
                    smallest_element = list_of_integers[iterator_var]
                    index_tracker = iterator_var
                iterator_var += 1
            output_sequence.append(smallest_element)
            del list_of_integers[index_tracker]
        else:
            largest_element = list_of_integers[0]
            idx_pointer = 0
            pos_counter = 1
            while pos_counter < len(list_of_integers):
                if list_of_integers[pos_counter] > largest_element:
                    largest_element = list_of_integers[pos_counter]
                    idx_pointer = pos_counter
                pos_counter += 1
            output_sequence.append(largest_element)
            del list_of_integers[idx_pointer]

        toggle_indicator = not toggle_indicator

    return output_sequence