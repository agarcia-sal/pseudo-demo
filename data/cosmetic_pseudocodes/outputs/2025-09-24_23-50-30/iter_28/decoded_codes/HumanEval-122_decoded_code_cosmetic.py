from typing import List, Union


def add_elements(collection_A: List[int], number_B: int) -> int:
    accumulator_C: int = 0

    def helper_D(index_E: int) -> int:
        nonlocal accumulator_C
        if index_E >= number_B:
            return accumulator_C
        if len(str(collection_A[index_E])) <= 2:
            accumulator_C += collection_A[index_E]
        return helper_D(index_E + 1)

    return helper_D(0)