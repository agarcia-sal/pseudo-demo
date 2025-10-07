from typing import List


def count_nums(arr: List[int]) -> int:
    def digits_sum(num: int) -> int:
        sign_flag: int = 1
        if num < 0:
            sign_flag = -1
            num = -num
        digits_str: str = str(num)
        digits_arr: List[int] = [int(d) for d in digits_str]
        digits_arr[0] *= sign_flag

        total: int = 0
        idx: int = 0
        while idx < len(digits_arr):
            total += digits_arr[idx]
            idx += 1
        return total

    sums: List[int] = []
    idx_outer: int = 0
    while idx_outer < len(arr):
        sums.append(digits_sum(arr[idx_outer]))
        idx_outer += 1

    positive_counts: int = 0
    idx_filter: int = 0
    while idx_filter < len(sums):
        if sums[idx_filter] > 0:
            positive_counts += 1
        idx_filter += 1

    return positive_counts