from typing import List


def triples_sum_to_zero(numbers_array: List[int]) -> bool:
    for iterator_a in range(len(numbers_array)):
        for iterator_b in range(iterator_a + 1, len(numbers_array)):
            for iterator_c in range(iterator_b + 1, len(numbers_array)):
                total_sum = (
                    numbers_array[iterator_a]
                    + numbers_array[iterator_b]
                    + numbers_array[iterator_c]
                )
                if total_sum == 0:
                    return True
    return False