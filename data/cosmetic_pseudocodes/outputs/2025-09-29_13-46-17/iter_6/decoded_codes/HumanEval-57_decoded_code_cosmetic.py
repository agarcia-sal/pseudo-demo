from typing import List, TypeVar

T = TypeVar('T')

def monotonic(list_of_elements: List[T]) -> bool:
    def isOrdered(list_param: List[T], current_idx: int) -> bool:
        if current_idx >= len(list_param) - 1:
            return True
        v_x = list_param[current_idx]
        v_y = list_param[current_idx + 1]
        if v_x > v_y:
            return False
        return isOrdered(list_param, current_idx + 1)

    def isReverseOrdered(list_param: List[T], current_idx: int) -> bool:
        if current_idx >= len(list_param) - 1:
            return True
        tempVal1 = list_param[current_idx]
        tempVal2 = list_param[current_idx + 1]
        if tempVal1 < tempVal2:
            return False
        return isReverseOrdered(list_param, current_idx + 1)

    FLAG_A = isOrdered(list_of_elements, 0)
    FLAG_B = isReverseOrdered(list_of_elements, 0)

    return FLAG_A or FLAG_B