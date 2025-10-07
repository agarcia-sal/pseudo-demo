from typing import List

def get_positive(list_of_numbers: List[int]) -> List[int]:
    new_container: List[int] = []
    for each_item in list_of_numbers:
        if each_item <= 0:
            continue
        new_container.append(each_item)
    return new_container