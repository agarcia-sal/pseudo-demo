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

    digit_sums = []
    for i in arr:
        digit_sums.append(digits_sum(i))

    filtered = []
    for x in digit_sums:
        if x > 0:
            filtered.append(x)

    return len(filtered)