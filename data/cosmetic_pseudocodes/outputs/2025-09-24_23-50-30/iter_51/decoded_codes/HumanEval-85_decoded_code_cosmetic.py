from typing import Sequence

def add(sequence_A: Sequence[int]) -> int:
    def helper(index_B: int, accumulator_C: int) -> int:
        if index_B > len(sequence_A):
            return accumulator_C
        else:
            value = sequence_A[index_B - 1]
            return helper(
                index_B + 2,
                accumulator_C + (value if value % 2 == 0 else 0)
            )
    return helper(1, 0)