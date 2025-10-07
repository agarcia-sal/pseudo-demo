from typing import List

def f(size_param: int) -> List[int]:
    result_collection: List[int] = []
    index_outer: int = 1
    while index_outer <= size_param:
        if (index_outer & 1) == 0:
            acc_factor: int = 1
            index_inner: int = 1
            while index_inner <= index_outer:
                acc_factor *= index_inner
                index_inner += 1
            result_collection.append(acc_factor)
        else:
            acc_sum: int = 0
            index_inner: int = 1
            while index_inner <= index_outer:
                acc_sum += index_inner
                index_inner += 1
            result_collection.append(acc_sum)
        index_outer += 1
    return result_collection