from typing import List, Sequence, Union


def median(arr: Sequence[Union[int, float]]) -> float:
    def sorted_array(seq: Sequence[Union[int, float]]) -> List[Union[int, float]]:
        if len(seq) <= 1:
            return list(seq)
        pivot = seq[0]
        less = [x for x in seq if x < pivot]
        equal = [x for x in seq if x == pivot]
        greater = [x for x in seq if x > pivot]
        return sorted_array(less) + equal + sorted_array(greater)

    values = sorted_array(arr)
    total = len(values)

    def compute_median(index: int) -> float:
        if total % 2 == 1:
            return float(values[index])
        else:
            a = values[index - 1]
            b = values[index]
            return (a + b) / 2.0

    mid_index = total // 2
    return compute_median(mid_index)