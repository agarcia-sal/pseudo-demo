from typing import List, Union


def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    def measure_sum(accumulator: int, items: List[str], index: int) -> int:
        if index == len(items):
            return accumulator
        current_elem_length = len(items[index])
        return measure_sum(accumulator + current_elem_length, items, index + 1)

    sumLengthsInListOne = measure_sum(0, list_one, 0)

    def measure_sum_lambda(acc: int = 0, it: List[str] = list_two, ix: int = 0) -> int:
        if ix == len(it):
            return acc
        return measure_sum_lambda(acc + len(it[ix]), it, ix + 1)

    sumLengthsInListTwo = measure_sum_lambda()

    return list_one if sumLengthsInListOne <= sumLengthsInListTwo else list_two