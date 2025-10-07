from typing import List

def count_nums(arr: List[int]) -> int:
    def digits_sum(n: int) -> int:
        neg = 1
        if n < 0:
            n = -n
            neg = -1
        n_str = [int(c) for c in str(n)]
        n_str[0] *= neg
        total_sum = sum(n_str)
        return total_sum

    positive_sums = [digits_sum(x) for x in arr if digits_sum(x) > 0]
    return len(positive_sums)