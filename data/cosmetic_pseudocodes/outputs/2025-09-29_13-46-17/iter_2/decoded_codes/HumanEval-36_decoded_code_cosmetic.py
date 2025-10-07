from typing import List


def fizz_buzz(integer_n: int) -> int:
    list_nums: List[int] = []

    def check_and_add(index: int) -> None:
        if index < integer_n:
            if index % 11 == 0 or index % 13 == 0:
                list_nums.append(index)
            check_and_add(index + 1)

    check_and_add(0)

    concatenated_str: str = ""

    def concat_numbers(pos: int) -> None:
        nonlocal concatenated_str
        if pos < len(list_nums):
            concatenated_str += str(list_nums[pos])
            concat_numbers(pos + 1)

    concat_numbers(0)

    count_of_sevens: int = 0

    def count_sevens_at(pos: int) -> None:
        nonlocal count_of_sevens
        if pos < len(concatenated_str):
            if concatenated_str[pos] == "7":
                count_of_sevens += 1
            count_sevens_at(pos + 1)

    count_sevens_at(0)

    return count_of_sevens