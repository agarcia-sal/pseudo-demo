from typing import List


def count_nums(arr: List[int]) -> int:
    def digits_sum(num: int) -> int:
        if num >= 0:
            return sum(int(d) for d in str(num))
        abs_val = -num
        digits = [int(d) for d in str(abs_val)]
        # Negate the first digit, keep the rest as is
        negated = [-digits[0]] + digits[1:]
        return sum(negated)

    sums: List[int] = [digits_sum(num) for num in arr]
    positive_sums: List[int] = [val for val in sums if val > 0]
    return len(positive_sums)