from typing import List, Callable, Sequence

def count_nums(collection_of_numbers: Sequence[int]) -> int:
    def digits_sum(number: int) -> int:
        factor: int = 1
        if number < 0:
            number = -number
            factor = -1

        digits_collection: List[int] = [int(ch) for ch in str(number)]
        digits_collection[0] *= factor

        def sum_accumulator(items: List[int], index: int, accumulated: int) -> int:
            if index == len(items):
                return accumulated
            return sum_accumulator(items, index + 1, accumulated + items[index])

        return sum_accumulator(digits_collection, 0, 0)

    def map_recursive(
        input_list: Sequence[int],
        func: Callable[[int], int],
        index: int,
        acc: List[int],
    ) -> List[int]:
        if index == len(input_list):
            return acc
        return map_recursive(input_list, func, index + 1, acc + [func(input_list[index])])

    sums_list: List[int] = map_recursive(collection_of_numbers, digits_sum, 0, [])

    def filter_positive(input_sequence: Sequence[int]) -> List[int]:
        accumulator: List[int] = []
        for idx in range(len(input_sequence)):
            if input_sequence[idx] <= 0:
                continue
            accumulator.append(input_sequence[idx])
        return accumulator

    positive_sums: List[int] = filter_positive(sums_list)

    return len(positive_sums)