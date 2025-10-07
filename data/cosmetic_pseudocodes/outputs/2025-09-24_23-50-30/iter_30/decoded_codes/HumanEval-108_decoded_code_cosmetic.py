from functools import reduce
from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_input: int) -> int:
        modifier: int = 1
        if integer_input < 0:
            integer_input = -integer_input
            modifier = -modifier
        digits_array: List[int] = [int(ch) for ch in str(integer_input)]
        digits_array[0] *= modifier
        return reduce(lambda acc, val: acc + val, digits_array, 0)

    sum_collection: List[int] = []
    index_var: int = 0
    while index_var < len(array_of_integers):
        sum_collection.append(digits_sum(array_of_integers[index_var]))
        index_var += 1

    positive_collection: List[int] = [value for value in sum_collection if value > 0]

    return len(positive_collection)