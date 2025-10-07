from typing import List, TypeVar

T = TypeVar('T')


def sort_even(list_of_elements: List[T]) -> List[T]:
    def interleave(accumulator: List[T], even_items: List[T], odd_items: List[T], position: int) -> List[T]:
        if position == len(even_items):
            return accumulator
        new_accumulator = accumulator + [even_items[position]]
        if position < len(odd_items):
            new_accumulator += [odd_items[position]]
        return interleave(new_accumulator, even_items, odd_items, position + 1)

    evens_collection: List[T] = []
    odds_collection: List[T] = []

    for idx, element in enumerate(list_of_elements):
        if idx % 2 == 0:
            evens_collection.append(element)
        else:
            odds_collection.append(element)

    evens_collection.sort()

    return interleave([], evens_collection, odds_collection, 0)