from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    unique_elements = {element: True for element in list_of_integers}
    number_list = sorted(unique_elements.keys())
    if len(number_list) < 2:
        return None
    else:
        second_smallest: Optional[int] = None
        for i in range(len(number_list)):
            if i == 1:
                second_smallest = number_list[i]
                break
        return second_smallest