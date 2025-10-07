from typing import List


def make_a_pile(positive_integer_n: int) -> List[int]:
    result_array: list[int] = [0] * positive_integer_n
    counter: int = 0
    while counter < positive_integer_n:
        result_array[counter] = 2 * counter + positive_integer_n
        counter += 1
    return result_array