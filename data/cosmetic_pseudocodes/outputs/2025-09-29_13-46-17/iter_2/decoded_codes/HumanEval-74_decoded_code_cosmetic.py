from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    def sum_lengths(collection: List[str], index: int, total: int) -> int:
        if index == len(collection):
            return total
        return sum_lengths(collection, index + 1, total + len(collection[index]))

    length_accumulator_1 = sum_lengths(list_one, 0, 0)
    length_accumulator_2 = sum_lengths(list_two, 0, 0)

    if not (length_accumulator_1 > length_accumulator_2):
        return list_one
    else:
        return list_two