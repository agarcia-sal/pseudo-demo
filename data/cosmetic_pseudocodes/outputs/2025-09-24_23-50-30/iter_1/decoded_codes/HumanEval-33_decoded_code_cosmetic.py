from typing import List, Sequence, TypeVar

T = TypeVar('T')

def sort_third(list_input: Sequence[T]) -> List[T]:
    temp_list: List[T] = list(list_input)
    indices_third: List[int] = [idx for idx in range(len(temp_list)) if idx % 3 == 0]
    sorted_section: List[T] = [temp_list[i] for i in indices_third]
    sorted_section.sort()
    for j, idx in enumerate(indices_third):
        temp_list[idx] = sorted_section[j]
    return temp_list