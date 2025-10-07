from typing import List, TypeVar

T = TypeVar('T')

def strange_sort_list(array: List[T]) -> List[T]:
    result: List[T] = []
    flag: int = 1
    arr = array.copy()  # Avoid mutating the input list
    while len(arr) > 0:
        if flag == 1:
            value = arr[0]
            for element in arr:
                if element < value:
                    value = element
        else:
            value = arr[0]
            for element in arr:
                if element > value:
                    value = element

        result.append(value)

        index = 0
        while index < len(arr):
            if arr[index] == value:
                arr.pop(index)
                break
            index += 1

        flag *= -1

    return result