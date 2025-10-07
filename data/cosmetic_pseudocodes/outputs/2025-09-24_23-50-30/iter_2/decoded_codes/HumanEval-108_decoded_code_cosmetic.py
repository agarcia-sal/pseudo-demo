from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        sign_multiplier: int
        if integer_value >= 0:
            sign_multiplier = 1
        else:
            sign_multiplier = -1
            integer_value = -integer_value

        def helper(index: int, digits_list: List[int]) -> int:
            if index == len(digits_list):
                return 0
            # Apply sign_multiplier only to the first digit
            current = digits_list[index] * (sign_multiplier if index == 0 else 1)
            return current + helper(index + 1, digits_list)

        digits_str = str(integer_value)
        digits_list = [int(d) for d in digits_str]

        return helper(0, digits_list)

    def map_digits_sum(arr: List[int], idx: int, acc: List[int]) -> List[int]:
        if idx == len(arr):
            return acc
        return map_digits_sum(arr, idx + 1, acc + [digits_sum(arr[idx])])

    all_sums = map_digits_sum(array_of_integers, 0, [])

    def count_positive(vals: List[int], position: int, count: int) -> int:
        if position == len(vals):
            return count
        if vals[position] <= 0:
            return count_positive(vals, position + 1, count)
        else:
            return count_positive(vals, position + 1, count + 1)

    return count_positive(all_sums, 0, 0)