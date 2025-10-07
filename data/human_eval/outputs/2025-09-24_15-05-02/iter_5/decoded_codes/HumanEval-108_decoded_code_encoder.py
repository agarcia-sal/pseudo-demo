from typing import List

def count_nums(arr: List[int]) -> int:
    def digits_sum(n: int) -> int:
        neg = 1
        if n < 0:
            n = -n
            neg = -1
        digits_list = [int(d) for d in str(n)]
        digits_list[0] *= neg
        return sum(digits_list)

    digit_sums = [digits_sum(element) for element in arr]
    filtered_list = [value for value in digit_sums if value > 0]
    return len(filtered_list)