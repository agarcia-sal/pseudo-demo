from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    first_sublist: List[T] = []
    second_sublist: List[T] = []
    idx: int = 0
    length: int = len(list_of_elements)

    while idx < length:
        if (idx // 2) * 2 == idx:
            first_sublist.append(list_of_elements[idx])
        else:
            second_sublist.append(list_of_elements[idx])
        idx += 1

    # Insertion sort on first_sublist (non-decreasing)
    i: int = 1
    while i < len(first_sublist):
        key_element = first_sublist[i]
        j = i - 1
        while j >= 0 and first_sublist[j] > key_element:
            first_sublist[j + 1] = first_sublist[j]
            j -= 1
        first_sublist[j + 1] = key_element
        i += 1

    combined_result: List[T] = []
    m: int = 0
    n: int = 0
    while m < len(first_sublist) and n < len(second_sublist):
        combined_result.append(first_sublist[m])
        combined_result.append(second_sublist[n])
        m += 1
        n += 1

    if len(first_sublist) > len(second_sublist):
        combined_result.append(first_sublist[-1])

    return combined_result