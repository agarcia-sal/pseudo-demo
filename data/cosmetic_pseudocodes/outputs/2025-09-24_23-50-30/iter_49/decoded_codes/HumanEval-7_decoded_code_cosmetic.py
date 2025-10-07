from typing import List

def filter_by_substring(input_array: List[str], target_fragment: str) -> List[str]:
    def helper_loop(indexer: int, accumulator: List[str]) -> List[str]:
        if indexer >= len(input_array):
            return accumulator
        if target_fragment in input_array[indexer]:
            accumulator.append(input_array[indexer])
        return helper_loop(indexer + 1, accumulator)
    return helper_loop(0, [])