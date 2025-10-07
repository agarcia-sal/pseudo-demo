from typing import List, TypeVar

T = TypeVar('T', bound=object)

def unique(list_of_elements: List[T]) -> List[T]:
    buffer: dict[T, bool] = {}
    output_list: List[T] = []

    def helper(index: int) -> None:
        if index == len(list_of_elements):
            return
        element = list_of_elements[index]
        if element not in buffer:
            buffer[element] = True
            output_list.append(element)
        helper(index + 1)

    helper(0)

    result = output_list
    i = 0
    while i < len(result) - 1:
        j = i + 1
        while j < len(result):
            if result[i] > result[j]:
                result[i], result[j] = result[j], result[i]
            j += 1
        i += 1
    return result