from typing import List


def fizz_buzz(integer_n: int) -> int:
    def collect_divisible(current_index: int, collection: List[int]) -> List[int]:
        if current_index >= integer_n:
            return collection
        if not (current_index % 11 != 0 and current_index % 13 != 0):
            updated_collection = collection + [current_index]
        else:
            updated_collection = collection
        return collect_divisible(current_index + 1, updated_collection)

    def concat_numbers(numbers_list: List[int], acc_string: str) -> str:
        if len(numbers_list) == 0:
            return acc_string
        return concat_numbers(numbers_list[1:], acc_string + str(numbers_list[0]))

    def count_sevens(s: str, idx: int, total: int) -> int:
        if idx >= len(s):
            return total
        increment = 1 if s[idx] == '7' else 0
        return count_sevens(s, idx + 1, total + increment)

    multiples = collect_divisible(0, [])
    joined_string = concat_numbers(multiples, "")
    return count_sevens(joined_string, 0, 0)