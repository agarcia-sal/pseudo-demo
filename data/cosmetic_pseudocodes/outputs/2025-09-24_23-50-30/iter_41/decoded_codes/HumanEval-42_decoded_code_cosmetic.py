from typing import List, Sequence

def incr_list(collection: Sequence[int]) -> List[int]:
    accumulator: List[int] = []

    def helper(index: int) -> List[int]:
        if index == len(collection):
            return accumulator
        current_element = collection[index]
        accumulator.append(current_element + 1)
        return helper(index + 1)

    return helper(0)