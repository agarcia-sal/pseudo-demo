from typing import List, TypeVar

T = TypeVar("T")

def sort_even(preserved_parameter: List[T]) -> List[T]:
    temp_storage_a: List[T] = []
    temp_storage_b: List[T] = []
    idx: int = 0

    while idx < len(preserved_parameter):
        if idx % 2 == 0:
            temp_storage_a.append(preserved_parameter[idx])
        else:
            temp_storage_b.append(preserved_parameter[idx])
        idx += 1

    temp_storage_a.sort()

    def interleave_rec(a_list: List[T], b_list: List[T], acc: List[T]) -> List[T]:
        if not a_list and not b_list:
            return acc
        if a_list and b_list:
            return interleave_rec(a_list[1:], b_list[1:], acc + [a_list[0], b_list[0]])
        if a_list:
            return interleave_rec(a_list[1:], b_list, acc + [a_list[0]])
        return interleave_rec(a_list, b_list[1:], acc + [b_list[0]])

    return interleave_rec(temp_storage_a, temp_storage_b, [])