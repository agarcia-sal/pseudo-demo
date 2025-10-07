from typing import List, TypeVar

T = TypeVar("T")


def sort_even(list_of_elements: List[T]) -> List[T]:
    even_positioned: List[T] = [e for i, e in enumerate(list_of_elements) if i % 2 == 0]
    odd_positioned: List[T] = [e for i, e in enumerate(list_of_elements) if i % 2 == 1]
    even_positioned.sort()

    merged_list: List[T] = []
    min_len = min(len(even_positioned), len(odd_positioned))
    for i in range(min_len):
        merged_list.append(even_positioned[i])
        merged_list.append(odd_positioned[i])
    if len(even_positioned) > len(odd_positioned):
        merged_list.append(even_positioned[-1])
    return merged_list