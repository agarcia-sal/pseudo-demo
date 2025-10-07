from typing import List


def count_nums(ns: List[int]) -> int:
    def digits_sum(val: int) -> int:
        sm = 1
        if val < 0:
            val = -val
            sm = -1

        digits_str = str(val)
        arr: List[int] = []
        idx = 0
        while idx < len(digits_str):
            ch = digits_str[idx]
            arr.append(int(ch))
            idx += 1

        arr[0] = arr[0] * sm

        total = 0
        j = 0
        while j < len(arr):
            total += arr[j]
            j += 1
        return total

    acc: List[int] = []
    i = 0
    while i < len(ns):
        cur = ns[i]
        temp = digits_sum(cur)
        acc.append(temp)
        i += 1

    res: List[int] = []
    k = 0
    while k < len(acc):
        if not (acc[k] > 0):
            k += 1
            continue
        else:
            res.append(acc[k])
            k += 1

    return len(res)