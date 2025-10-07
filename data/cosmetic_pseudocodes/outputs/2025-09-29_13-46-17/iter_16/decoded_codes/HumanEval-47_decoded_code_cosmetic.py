from typing import List, TypeVar, Callable

T = TypeVar('T', bound=float)  # assuming elements are numeric for median calculation

def median(list_of_elements: List[T]) -> float:
    def nth_element(sorted_list: List[T], index: int) -> T:
        # Recursive retrieval of the nth element
        return sorted_list[0] if index == 0 else nth_element(sorted_list[1:], index - 1)

    def insert_sorted(element: T, sorted_list: List[T]) -> List[T]:
        # Insert element into sorted_list preserving order (ascending)
        if not sorted_list or element <= sorted_list[0]:
            return [element] + sorted_list
        return [sorted_list[0]] + insert_sorted(element, sorted_list[1:])

    def foldr(func: Callable[[T, List[T]], List[T]], acc: List[T], lst: List[T]) -> List[T]:
        # Right fold: process list from right to left
        if not lst:
            return acc
        return func(lst[-1], foldr(func, acc, lst[:-1]))

    sorted_list: List[T] = foldr(insert_sorted, [], list_of_elements)

    def μ⨂(βϟ: List[T]) -> float:
        n = len(βϟ)
        if (n % 2) != 0:
            return float(nth_element(βϟ, n // 2))
        else:
            ζϠ = nth_element(βϟ, (n // 2) - 1)
            ϴʭ = nth_element(βϟ, n // 2)
            return (ζϠ + ϴʭ) * 0.5

    return μ⨂(sorted_list)