from typing import List

def incr_list(array_input: List[int]) -> List[int]:
    result_accumulator: List[int] = []

    def recursive_increment(position: int) -> None:
        if position < len(array_input):
            result_accumulator.append(array_input[position] + 1)
            recursive_increment(position + 1)
        else:
            return

    recursive_increment(0)
    return result_accumulator