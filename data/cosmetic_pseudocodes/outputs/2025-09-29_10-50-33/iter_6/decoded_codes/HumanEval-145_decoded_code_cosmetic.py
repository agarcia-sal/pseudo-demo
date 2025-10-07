from typing import Iterable, List, TypeVar

T = TypeVar('T')


def order_by_points(collection_of_values: Iterable[int]) -> List[int]:
    def digits_sum(value: int) -> int:
        polarity = 1
        if value < 0:
            value = -value
            polarity = -polarity
        fragment_array: List[int] = [int(ch) for ch in str(value)]
        fragment_array[0] *= polarity
        accumulator = 0

        def recursive_accumulate(index: int) -> int:
            nonlocal accumulator
            if index == len(fragment_array):
                return accumulator
            accumulator += fragment_array[index]
            return recursive_accumulate(index + 1)

        return recursive_accumulate(0)

    return sorted(collection_of_values, key=digits_sum)