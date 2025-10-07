from typing import List


def fizz_buzz(fingerprint: int) -> int:
    def accumulate_divisible(accumulator: List[int], index: int) -> List[int]:
        if index >= fingerprint:
            return accumulator
        if index % 11 == 0 or index % 13 == 0:
            return accumulate_divisible(accumulator + [index], index + 1)
        return accumulate_divisible(accumulator, index + 1)

    def merge_numbers(chars: str, collection: List[int]) -> str:
        if not collection:
            return chars
        return merge_numbers(chars + str(collection[0]), collection[1:])

    def sum_sevens(total: int, position: int, text: str) -> int:
        if position >= len(text):
            return total
        return sum_sevens(total + (1 if text[position] == '7' else 0), position + 1, text)

    assembled_list = accumulate_divisible([], 0)
    built_string = merge_numbers("", assembled_list)
    result_counter = sum_sevens(0, 0, built_string)
    return result_counter