from typing import Sequence, List


def count_nums(sequence_of_values: Sequence[int]) -> int:
    def digits_sum(number: int) -> int:
        factor = 1
        if number < 0:
            number = -number
            factor = -factor
        digits_array: List[int] = [int(d) for d in str(number)]
        digits_array[0] *= factor
        total = sum(digits_array)
        return total

    results_collection: List[int] = [digits_sum(item) for item in sequence_of_values]
    positive_only = [elem for elem in results_collection if elem > 0]
    return len(positive_only)