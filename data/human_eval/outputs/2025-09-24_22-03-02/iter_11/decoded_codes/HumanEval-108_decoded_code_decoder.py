from typing import List

def count_nums(arr: List[int]) -> int:
    def digits_sum(n: int) -> int:
        neg = 1
        if n < 0:
            n = -n
            neg = -1
        digits = list(map(int, str(n)))
        digits[0] *= neg
        return sum(digits)

    sums = [digits_sum(i) for i in arr]
    filtered = [x for x in sums if x > 0]
    return len(filtered)