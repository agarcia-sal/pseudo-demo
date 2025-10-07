from typing import List


def count_nums(arr: List[int]) -> int:
    def digits_sum(n: int) -> int:
        neg = 1
        if n < 0:
            n = -n
            neg = -1
        digits: List[int] = [int(ch) for ch in str(n)]
        digits[0] *= neg
        return sum(digits)

    sums_list: List[int] = [digits_sum(element) for element in arr]
    filtered_list: List[int] = [x for x in sums_list if x > 0]
    return len(filtered_list)