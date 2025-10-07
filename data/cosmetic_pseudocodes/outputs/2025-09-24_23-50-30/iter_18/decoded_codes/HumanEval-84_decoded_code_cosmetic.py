from typing import List


def solve(integer_N: int) -> str:
    digits_collection: List[str] = list(str(integer_N))
    accumulator: int = 0
    index_counter: int = 0
    while index_counter < len(digits_collection):
        current_element: str = digits_collection[index_counter]
        accumulator += int(current_element)
        index_counter += 1
    binary_full_string: str = bin(accumulator)
    result_string: str = binary_full_string[3:]
    return result_string