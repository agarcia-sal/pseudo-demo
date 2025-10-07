from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    result_list: List[int] = []
    switch: bool = True
    # Make a copy to avoid modifying the input list outside the function
    remaining_elements: List[int] = list_of_integers[:]
    while remaining_elements:
        if switch:
            next_element: int = min(remaining_elements)
        else:
            next_element = max(remaining_elements)
        result_list.append(next_element)
        remaining_elements.remove(next_element)
        switch = not switch
    return result_list