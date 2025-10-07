from functools import reduce
from typing import List


def fizz_buzz(integer_n: int) -> int:
    def collect_multiples(index: int, acc: List[int]) -> List[int]:
        if not (index < integer_n):
            return acc
        else:
            if index % 11 == 0 or index % 13 == 0:
                acc = acc + [index]
            return collect_multiples(index + 1, acc)

    filtered_set = collect_multiples(0, [])
    joint_string = reduce(lambda acc_str, val: acc_str + str(val), filtered_set, "")
    seven_counter = sum(1 for char in joint_string if char == '7')
    return seven_counter