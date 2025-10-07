from typing import List, Union, Tuple


def pluck(eta: List[int]) -> Union[List[int], List[Union[int, int]]]:
    def find_min_and_index(xs: List[int], idx: int, acc_val: int, acc_idx: int) -> List[Union[int, int]]:
        if idx >= len(xs):
            return [acc_val, acc_idx]
        curr_val = xs[idx]
        if curr_val < acc_val:
            return find_min_and_index(xs, idx + 1, curr_val, idx)
        else:
            return find_min_and_index(xs, idx + 1, acc_val, acc_idx)

    def filter_evens(arr: List[int], pos: int, res: List[int]) -> List[int]:
        if pos >= len(arr):
            return res
        val = arr[pos]
        if val % 2 == 0:
            return filter_evens(arr, pos + 1, res + [val])
        else:
            return filter_evens(arr, pos + 1, res)

    zed = filter_evens(eta, 0, [])

    if len(eta) == 0:
        return []
    if len(zed) == 0:
        return []

    min_val_and_idx = find_min_and_index(eta, 0, zed[0], eta.index(zed[0]))
    return min_val_and_idx