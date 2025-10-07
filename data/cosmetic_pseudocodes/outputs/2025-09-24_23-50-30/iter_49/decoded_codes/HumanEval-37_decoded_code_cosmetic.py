from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    even_series: List[T] = []
    odd_series: List[T] = []
    cursor: int = 0

    while cursor < len(list_of_elements):
        if cursor % 2 == 0:
            even_series.append(list_of_elements[cursor])
        else:
            odd_series.append(list_of_elements[cursor])
        cursor += 1

    even_series.sort()  # sort_in_place ascending=True by default

    def build_answer(accumulator: List[T], idx: int) -> List[T]:
        if idx >= len(even_series):
            return accumulator
        if idx < len(odd_series):
            return build_answer(accumulator + [even_series[idx], odd_series[idx]], idx + 1)
        else:
            return build_answer(accumulator + [even_series[idx]], idx + 1)

    return build_answer([], 0)