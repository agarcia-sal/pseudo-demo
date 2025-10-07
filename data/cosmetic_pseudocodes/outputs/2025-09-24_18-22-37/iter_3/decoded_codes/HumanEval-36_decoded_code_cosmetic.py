from typing import List


def fizz_buzz(integer_n: int) -> int:
    def helper_collect(accumulated: List[int], current: int) -> List[int]:
        if current >= integer_n:
            return accumulated
        if current % 11 == 0 or current % 13 == 0:
            return helper_collect(accumulated + [current], current + 1)
        return helper_collect(accumulated, current + 1)

    filtered_numbers = helper_collect([], 0)

    def concat_all(elements: List[int], index: int) -> str:
        if index == len(elements):
            return ""
        return str(elements[index]) + concat_all(elements, index + 1)

    all_numbers_concatenated = concat_all(filtered_numbers, 0)

    sevens_counter = 0
    pos = 0
    length = len(all_numbers_concatenated)
    while pos < length:
        if all_numbers_concatenated[pos] == '7':
            sevens_counter += 1
        pos += 1

    return sevens_counter