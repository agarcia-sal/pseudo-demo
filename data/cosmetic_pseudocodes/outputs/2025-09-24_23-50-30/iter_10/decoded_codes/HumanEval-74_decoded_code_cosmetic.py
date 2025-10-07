from typing import List, Sequence

def total_match(list_one: Sequence[Sequence], list_two: Sequence[Sequence]) -> Sequence[Sequence]:
    def sum_lengths(collection: Sequence[Sequence]) -> int:
        return sum(len(element) for element in collection)

    first_total = sum_lengths(list_one)
    second_total = sum_lengths(list_two)

    if first_total <= second_total:
        return list_one
    return list_two