from typing import List, TypeVar, Union

T = TypeVar('T', bound=Union[int, float])

def median(list_of_elements: List[T]) -> float:
    # Copy elements into a new list
    sorted_array: List[T] = []
    for item in list_of_elements:
        sorted_array.append(item)

    # Sort the array using selection sort
    index = 0
    length = len(sorted_array)
    while index < length - 1:
        j = index + 1
        while j < length:
            if sorted_array[index] > sorted_array[j]:
                sorted_array[index], sorted_array[j] = sorted_array[j], sorted_array[index]
            j += 1
        index += 1

    n = length
    # If (n + 1) is even i.e. n is odd, return middle element
    if (n + 1) % 2 == 0:
        return float(sorted_array[(n - 1) // 2])

    left_index = (n // 2) - 1
    right_index = n // 2
    # Average the two middle values
    return (sorted_array[left_index] + sorted_array[right_index]) / 2.0