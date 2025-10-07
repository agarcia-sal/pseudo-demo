from typing import List

def count_nums(arr: List[int]) -> int:
    def digits_sum(n: int) -> int:
        neg = 1
        if n < 0:
            n = -n
            neg = -1
        n_list = [int(d) for d in str(n)]
        n_list[0] *= neg
        return sum(n_list)

    sums = []
    for i in arr:
        sums.append(digits_sum(i))

    filtered_sums = []
    for x in sums:
        if x > 0:
            filtered_sums.append(x)

    return len(filtered_sums)