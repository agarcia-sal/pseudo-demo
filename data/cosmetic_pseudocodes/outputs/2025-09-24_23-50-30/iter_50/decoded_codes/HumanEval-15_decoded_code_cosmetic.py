from functools import reduce
from typing import List

def string_sequence(integer_n: int) -> str:
    def append_string(accumulator_list: List[str], current_number: int, upper_bound: int) -> List[str]:
        if current_number > upper_bound:
            return accumulator_list
        new_accumulator = accumulator_list + [str(current_number)]
        return append_string(new_accumulator, current_number + 1, upper_bound)

    result_list = append_string([], 0, integer_n)
    sequence_string = reduce(lambda acc, cur: cur if acc == "" else acc + " " + cur, result_list, "")
    return sequence_string