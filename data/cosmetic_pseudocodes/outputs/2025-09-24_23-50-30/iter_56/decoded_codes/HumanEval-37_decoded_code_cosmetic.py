from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    temp_list_a: List[T] = []
    temp_list_b: List[T] = []
    idx_c: int = 0
    while idx_c < len(list_of_elements):
        if idx_c % 2 == 0:
            temp_list_a.append(list_of_elements[idx_c])
        else:
            temp_list_b.append(list_of_elements[idx_c])
        idx_c += 1

    def iterative_sort(array_X: List[T]) -> List[T]:
        limit_Y = len(array_X)
        pos_Z = 1
        while pos_Z < limit_Y:
            key_W = array_X[pos_Z]
            idx_V = pos_Z - 1
            while idx_V >= 0 and array_X[idx_V] > key_W:
                array_X[idx_V + 1] = array_X[idx_V]
                idx_V -= 1
            array_X[idx_V + 1] = key_W
            pos_Z += 1
        return array_X

    sorted_even = iterative_sort(temp_list_a)

    accumulator_M: List[T] = []
    idx_N = 0
    while idx_N < len(temp_list_b) and idx_N < len(sorted_even):
        accumulator_M.append(sorted_even[idx_N])
        accumulator_M.append(temp_list_b[idx_N])
        idx_N += 1

    if len(sorted_even) > len(temp_list_b):
        accumulator_M.append(sorted_even[len(sorted_even) - 1])

    return accumulator_M