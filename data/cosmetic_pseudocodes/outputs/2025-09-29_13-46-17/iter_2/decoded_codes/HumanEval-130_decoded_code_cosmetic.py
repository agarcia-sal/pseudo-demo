from typing import List


def tri(integer_n: int) -> List[int]:
    return tri_helper(integer_n, [1, 3], 2)


def tri_helper(num: int, arr: List[int], idx: int) -> List[int]:
    if num == 0:
        return [1]
    if idx > num:
        return arr
    if idx % 2 != 1:
        val = (idx // 2) + 1
    else:
        val = arr[idx - 1] + arr[idx - 2] + ((idx + 3) // 2)
    return tri_helper(num, arr + [val], idx + 1)