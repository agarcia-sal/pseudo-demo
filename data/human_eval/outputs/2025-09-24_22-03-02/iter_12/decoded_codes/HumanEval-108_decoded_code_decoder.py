from typing import List

def count_nums(arr: List[int]) -> int:
    def digits_sum(n: int) -> int:
        neg = 1
        if n < 0:
            n = n * -1
            neg = -1
        n = [int(d) for d in str(n)]
        n[0] = n[0] * neg
        return sum(n)

    digits_sums: List[int] = []
    for i in arr:
        digits_sums.append(digits_sum(i))
    filtered: List[int] = []
    for x in digits_sums:
        if x > 0:
            filtered.append(x)
    return len(filtered)