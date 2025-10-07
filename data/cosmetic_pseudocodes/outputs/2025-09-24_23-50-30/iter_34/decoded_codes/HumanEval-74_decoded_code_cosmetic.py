from typing import List, Sized, TypeVar

T = TypeVar('T', bound=Sized)

def total_match(list_one: List[T], list_two: List[T]) -> List[T]:
    count_x: int = 0
    for idx_x in range(len(list_one)):
        elem_x = list_one[idx_x]
        count_x += len(elem_x)

    count_y: int = 0
    for idx_y in range(len(list_two)):
        elem_y = list_two[idx_y]
        count_y += len(elem_y)

    if not (count_x > count_y):
        return list_one
    else:
        return list_two