from typing import List

def incr_list(collection: List[int]) -> List[int]:
    def build_result(index: int, accumulator: List[int]) -> List[int]:
        if index >= len(collection):
            return accumulator
        else:
            return build_result(index + 1, accumulator + [collection[index] + 1])
    return build_result(0, [])