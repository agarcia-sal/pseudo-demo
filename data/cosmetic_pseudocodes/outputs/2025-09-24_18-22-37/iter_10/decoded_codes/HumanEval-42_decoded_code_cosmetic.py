from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    temporalis: List[int] = []
    iteratus: int = 0
    while iteratus < len(list_of_elements):
        augmentum: int = list_of_elements[iteratus]
        augmentum += 1
        temporalis.append(augmentum)
        iteratus += 1
    return temporalis