from typing import List, TypeVar

T = TypeVar('T', bound='Comparable')

class Comparable:
    def __lt__(self, other: 'Comparable') -> bool:
        return NotImplemented

def sort_third(list_input: List[T]) -> List[T]:
    temp_list: List[T] = list_input[:]
    filtered_elements: List[T] = [temp_list[i] for i in range(len(temp_list)) if i % 3 == 0]
    ordered_elements: List[T] = sorted(filtered_elements)
    position = 0
    for j in range(len(temp_list)):
        if j % 3 == 0:
            temp_list[j] = ordered_elements[position]
            position += 1
    return temp_list