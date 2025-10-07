from typing import List

def count_nums(arr: List[int]) -> int:
    def digits_sum(n: int) -> int:
        neg = 1
        if n < 0:
            n = -n
            neg = -1
        digits = [int(d) for d in str(n)]
        digits[0] *= neg
        return sum(digits)

    list_of_sums: List[int] = [digits_sum(element) for element in arr]
    filtered_list: List[int] = [x for x in list_of_sums if x > 0]
    return len(filtered_list)