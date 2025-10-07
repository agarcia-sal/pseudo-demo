from typing import List

def count_nums(arr: List[int]) -> int:
    def digits_sum(val: int) -> int:
        sign = 1
        if val < 0:
            val = -val
            sign = -1

        digits_str = str(val)
        digits_arr = [int(d) for d in digits_str]

        if digits_arr:
            digits_arr[0] *= sign

        return sum(digits_arr)

    sums_collection: List[int] = []
    idx = 0
    while idx < len(arr):
        sums_collection.append(digits_sum(arr[idx]))
        idx += 1

    positive_vals = [x for x in sums_collection if x > 0]

    return len(positive_vals)