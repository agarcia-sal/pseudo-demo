from typing import Sequence, List


def derivative(sequence_of_constants: Sequence[int]) -> List[int]:
    def helper(iterator: Sequence[int], accumulator: List[int]) -> List[int]:
        if not iterator:
            return accumulator
        return helper(
            iterator[1:], 
            accumulator + [iterator[0] * (len(sequence_of_constants) - len(iterator))]
        )
    return helper(sequence_of_constants[1:], [])