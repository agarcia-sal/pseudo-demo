from typing import List, Iterable

def incr_list(container_collection: Iterable[int]) -> List[int]:
    def helper(iterator_source: Iterable[int], accumulator_result: List[int]) -> List[int]:
        it = iter(iterator_source)
        try:
            head = next(it)
        except StopIteration:
            return accumulator_result
        return helper(it, accumulator_result + [head + 1])
    return helper(container_collection, [])