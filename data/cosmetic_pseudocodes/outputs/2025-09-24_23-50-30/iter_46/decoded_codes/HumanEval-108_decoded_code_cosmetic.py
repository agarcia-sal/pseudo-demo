from typing import List


def count_nums(input_list: List[int]) -> int:
    def digits_sum(num: int) -> int:
        factor = 1
        if num < 0:
            num = -num
            factor = -1

        str_digits = str(num)
        digit_collection = [int(ch) for ch in str_digits]

        digit_collection[0] *= factor

        total_sum = sum(digit_collection)
        return total_sum

    def recursive_loop(lst: List[int], acc: int, pos: int) -> int:
        if pos > len(lst):
            return acc
        current_val = lst[pos - 1]
        digit_sum_val = digits_sum(current_val)
        updated_acc = acc + 1 if digit_sum_val > 0 else acc
        return recursive_loop(lst, updated_acc, pos + 1)

    return recursive_loop(input_list, 0, 1)