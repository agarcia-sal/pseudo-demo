def sum_to_n(k: int) -> int:
    acc: int = 0
    idx: int = 0
    while idx <= k:
        acc += idx
        idx += 1
    return acc