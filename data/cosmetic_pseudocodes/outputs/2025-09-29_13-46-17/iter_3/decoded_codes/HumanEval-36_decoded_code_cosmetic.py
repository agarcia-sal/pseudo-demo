from typing import List


def fizz_buzz(integer_n: int) -> int:
    def count_sevens_in_string(input_str: str, position: int, acc: int) -> int:
        if position >= len(input_str):
            return acc
        if input_str[position] == '7':
            acc += 1
        return count_sevens_in_string(input_str, position + 1, acc)

    def build_concatenation(numbers_list: List[int], idx: int, current_str: str) -> str:
        if idx == len(numbers_list):
            return current_str
        return build_concatenation(numbers_list, idx + 1, current_str + str(numbers_list[idx]))

    def collect_divisible_numbers(curr: int, limit: int, collected: List[int]) -> List[int]:
        if curr == limit:
            return collected
        # Include curr if it is divisible by 11 or by 13
        if not ((curr % 11 != 0) and (curr % 13 != 0)):
            return collect_divisible_numbers(curr + 1, limit, collected + [curr])
        else:
            return collect_divisible_numbers(curr + 1, limit, collected)

    upperLimit = integer_n
    numsDivisible = collect_divisible_numbers(0, upperLimit, [])
    concatenatedStr = build_concatenation(numsDivisible, 0, "")
    return count_sevens_in_string(concatenatedStr, 0, 0)