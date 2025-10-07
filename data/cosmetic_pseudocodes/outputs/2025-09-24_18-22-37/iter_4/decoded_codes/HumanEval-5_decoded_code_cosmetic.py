from typing import List, TypeVar

T = TypeVar('T')

def intersperse(list_of_numbers: List[T], delimiter: T) -> List[T]:
    result_list: List[T] = []
    index: int = 0
    count: int = len(list_of_numbers)

    if count == 0:
        return result_list

    while index < count - 1:
        result_list.append(list_of_numbers[index])
        result_list.append(delimiter)
        index += 1

    result_list.append(list_of_numbers[count - 1])

    return result_list