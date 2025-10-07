from typing import List


def fizz_buzz(integer_n: int) -> int:
    def helper_collect(curr_index: int, acc_list: List[int]) -> List[int]:
        # Include curr_index if divisible by 11 or 13
        if not ((curr_index % 11 != 0) and (curr_index % 13 != 0)):
            acc_list.append(curr_index)
        if curr_index + 1 < integer_n:
            return helper_collect(curr_index + 1, acc_list)
        return acc_list

    list_of_numbers: List[int] = helper_collect(0, [])

    def helper_concat(idx: int, lst: List[int], acc_str: str) -> str:
        if idx >= len(lst):
            return acc_str
        return helper_concat(idx + 1, lst, acc_str + str(lst[idx]))

    concatenated_string: str = helper_concat(0, list_of_numbers, "")

    def count_sevens_in_string(s: str) -> int:
        count = 0
        idx = 0
        while idx < len(s):
            if s[idx] == '7':
                count += 1
            idx += 1
        return count

    return count_sevens_in_string(concatenated_string)