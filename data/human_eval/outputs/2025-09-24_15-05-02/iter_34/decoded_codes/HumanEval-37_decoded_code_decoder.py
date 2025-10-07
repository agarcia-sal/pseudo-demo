from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    even_indexed_elements = list_of_elements[0::2]
    odd_indexed_elements = list_of_elements[1::2]
    even_indexed_elements_sorted = sorted(even_indexed_elements)
    answer_list: List[T] = []
    for pair_of_elements in zip(even_indexed_elements_sorted, odd_indexed_elements):
        answer_list.extend(pair_of_elements)
    if len(even_indexed_elements_sorted) > len(odd_indexed_elements):
        answer_list.append(even_indexed_elements_sorted[-1])
    return answer_list