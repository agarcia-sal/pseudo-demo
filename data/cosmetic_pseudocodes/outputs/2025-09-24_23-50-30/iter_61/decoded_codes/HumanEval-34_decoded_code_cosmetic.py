from typing import List, TypeVar

T = TypeVar('T')

def unique(parameter_one: List[T]) -> List[T]:
    temporary_list: List[T] = sorted(parameter_one)
    result_list: List[T] = []
    while temporary_list:
        # Since the switch case is always case 1, we execute this block every time
        if not result_list or temporary_list[0] != result_list[-1]:
            result_list.append(temporary_list[0])
        temporary_list = temporary_list[1:]
    return result_list