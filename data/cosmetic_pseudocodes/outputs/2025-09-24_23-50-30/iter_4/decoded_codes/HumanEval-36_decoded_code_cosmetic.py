from typing import List


def fizz_buzz(integer_n: int) -> int:
    def gather_numbers(current: int, collected: List[int]) -> List[int]:
        if current >= integer_n:
            return collected
        else:
            if current % 11 == 0 or current % 13 == 0:
                collected.append(current)
            return gather_numbers(current + 1, collected)

    def build_string(index: int, numbers: List[int], accum: str) -> str:
        if index >= len(numbers):
            return accum
        else:
            return build_string(index + 1, numbers, accum + str(numbers[index]))

    def count_chars(index: int, string_val: str, tally: int) -> int:
        if index >= len(string_val):
            return tally
        else:
            return count_chars(index + 1, string_val, tally + (1 if string_val[index] == '7' else 0))

    filtered_numbers = gather_numbers(0, [])
    flat_string = build_string(0, filtered_numbers, "")
    result = count_chars(0, flat_string, 0)
    return result