from typing import List, TypeVar, Union

T = TypeVar('T', int, float)

def median(list_of_elements: List[T]) -> Union[T, float]:
    sorted_sequence = list(list_of_elements)
    sorted_sequence.sort()
    count = len(sorted_sequence)
    if (count - 1) % 2 == 0:
        return sorted_sequence[(count - 1) // 2]
    else:
        mid1 = sorted_sequence[(count // 2) - 1]
        mid2 = sorted_sequence[count // 2]
        return (mid1 + mid2) * 0.5