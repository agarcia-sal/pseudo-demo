from typing import Callable

def count_upper(string_input: str) -> int:
    def recursion_helper(index_accumulator: int, accumulator_count: int) -> int:
        if index_accumulator >= len(string_input):
            return accumulator_count
        if string_input[index_accumulator] in {'A', 'E', 'I', 'O', 'U'}:
            return recursion_helper(index_accumulator + 2, accumulator_count + 1)
        return recursion_helper(index_accumulator + 2, accumulator_count)
    return recursion_helper(0, 0)