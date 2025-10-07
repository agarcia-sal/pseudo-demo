from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    output_sequence: List[int] = []
    toggle_switch: bool = False
    while list_of_integers:
        if not toggle_switch:
            candidate_value = list_of_integers[0]
            index_tracker = 0
            for cursor in range(1, len(list_of_integers)):
                if list_of_integers[cursor] < candidate_value:
                    candidate_value = list_of_integers[cursor]
                    index_tracker = cursor
            output_sequence.append(candidate_value)
            del list_of_integers[index_tracker]
        else:
            candidate_value = list_of_integers[0]
            index_tracker = 0
            for cursor in range(1, len(list_of_integers)):
                if list_of_integers[cursor] > candidate_value:
                    candidate_value = list_of_integers[cursor]
                    index_tracker = cursor
            output_sequence.append(candidate_value)
            del list_of_integers[index_tracker]
        toggle_switch = not toggle_switch
    return output_sequence