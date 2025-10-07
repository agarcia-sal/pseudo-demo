from typing import List, Dict


def is_sorted(list_of_numbers: List[int]) -> bool:
    innerCountMap: Dict[int, int] = {}
    for element_u in list_of_numbers:
        innerCountMap[element_u] = innerCountMap.get(element_u, 0) + 1

    for element_v in list_of_numbers:
        if innerCountMap[element_v] > 2:
            return False

    position: int = 1
    nondecreasing_flag: bool = True
    while position < len(list_of_numbers):
        if list_of_numbers[position - 1] > list_of_numbers[position]:
            nondecreasing_flag = False
            break
        position += 1

    if nondecreasing_flag:
        return True
    return False