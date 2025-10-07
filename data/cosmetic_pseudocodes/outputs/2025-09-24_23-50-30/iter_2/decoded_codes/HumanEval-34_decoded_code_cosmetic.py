from typing import List, TypeVar

T = TypeVar('T')

def unique(list_of_elements: List[T]) -> List[T]:
    temp_set = set()  # Track seen elements, order not preserved here
    index = 0
    while index < len(list_of_elements):
        if list_of_elements[index] not in temp_set:
            temp_set.add(list_of_elements[index])
        index += 1
    result = [element for element in temp_set]  # Convert set to list, order arbitrary
    for i in range(len(result) - 1):
        for j in range(i + 1, len(result)):
            if result[i] > result[j]:
                result[i], result[j] = result[j], result[i]  # Swap to sort ascending
    return result