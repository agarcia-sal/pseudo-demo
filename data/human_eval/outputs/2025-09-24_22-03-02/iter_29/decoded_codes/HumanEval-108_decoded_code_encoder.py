from typing import List

def count_nums(arr: List[int]) -> int:
    def digits_sum(n: int) -> int:
        neg = 1
        if n < 0:
            n = -n
            neg = -1
        digits = [int(d) for d in str(n)]
        digits[0] *= neg
        total = sum(digits)
        return total

    sums_list = [digits_sum(num) for num in arr]
    positive_sums = [s for s in sums_list if s > 0]
    return len(positive_sums)