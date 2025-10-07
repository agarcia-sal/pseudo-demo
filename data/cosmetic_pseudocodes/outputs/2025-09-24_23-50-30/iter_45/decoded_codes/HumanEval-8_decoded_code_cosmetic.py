from typing import Sequence, Tuple

def sum_product(collection_of_numbers: Sequence[int]) -> Tuple[int, int]:
    def accumulate(index: int, aggregate_sum: int, aggregate_product: int) -> Tuple[int, int]:
        if index >= len(collection_of_numbers):
            return aggregate_sum, aggregate_product
        return accumulate(index + 1,
                          aggregate_sum + collection_of_numbers[index],
                          aggregate_product * collection_of_numbers[index])
    return accumulate(0, 0, 1)