from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    altered_list: List[T] = list_input[:]

    def collect(index: int, accum: List[T]) -> List[T]:
        if index >= len(altered_list):
            return accum
        return collect(index + 3, accum + [altered_list[index]])

    extracted_elements: List[T] = collect(0, [])

    n: int = len(extracted_elements)
    i: int = 1
    while i < n:
        key: T = extracted_elements[i]
        j: int = i - 1
        while j >= 0 and extracted_elements[j] > key:
            extracted_elements[j + 1] = extracted_elements[j]
            j -= 1
        extracted_elements[j + 1] = key
        i += 1

    def replace(index: int, elems: List[T]) -> List[T]:
        if index >= len(altered_list):
            return altered_list
        altered_list[index] = elems[0]
        return replace(index + 3, elems[1:])

    replace(0, extracted_elements)

    return altered_list