from typing import List


def maximum(arr_ints: List[int], pos_int_k: int) -> List[int]:
    def sort_non_decreasing(A: List[int]) -> None:
        n = len(A)
        swapped = True
        while swapped:
            swapped = False
            idx = 0
            while idx < n - 1:
                if A[idx] > A[idx + 1]:
                    A[idx], A[idx + 1] = A[idx + 1], A[idx]
                    swapped = True
                idx += 1
            n -= 1

    if pos_int_k != 0:
        sort_non_decreasing(arr_ints)
        len_arr = len(arr_ints)
        start_pos = len_arr - pos_int_k
        res_list: List[int] = []
        i = start_pos
        while i < len_arr:
            res_list.append(arr_ints[i])
            i += 1
        return res_list
    else:
        return []