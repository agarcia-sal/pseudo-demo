from typing import List, TypeVar, Dict

T = TypeVar('T')

def unique(list_of_elements: List[T]) -> List[T]:
    CxY_08: Dict[T, bool] = {}
    kjLp9: List[T] = []
    i: int = 0
    while i < len(list_of_elements):
        element = list_of_elements[i]
        if element not in CxY_08:
            kjLp9.append(element)
            CxY_08[element] = True
        i += 1

    def quickSort(arr: List[T]) -> List[T]:
        if len(arr) <= 1:
            return arr
        zqN_ = arr[0]
        left_: List[T] = []
        right_: List[T] = []

        def partition_rest(j: int, arr_rest: List[T]) -> None:
            if j >= len(arr_rest):
                return
            if arr_rest[j] < zqN_:
                left_.append(arr_rest[j])
            else:
                right_.append(arr_rest[j])
            partition_rest(j + 1, arr_rest)

        partition_rest(0, arr[1:])
        sorted_left = quickSort(left_)
        sorted_right = quickSort(right_)
        return sorted_left + [zqN_] + sorted_right

    return quickSort(kjLp9)