from typing import List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    def has_zero(seq: List[int], index: int) -> bool:
        if index == len(seq):
            return False
        return seq[index] == 0 or has_zero(seq, index + 1)

    def neg_count(seq: List[int], idx: int, acc: int) -> int:
        if idx == len(seq):
            return acc
        if seq[idx] < 0:
            return neg_count(seq, idx + 1, acc + 1)
        return neg_count(seq, idx + 1, acc)

    def abs_sum(seq: List[int], pos: int, accumulator: int) -> int:
        if pos == len(seq):
            return accumulator
        val = -seq[pos] if seq[pos] < 0 else seq[pos]
        return abs_sum(seq, pos + 1, accumulator + val)

    if not array_of_integers:
        return None

    if has_zero(array_of_integers, 0):
        var_a = 0
    else:
        var_b = neg_count(array_of_integers, 0, 0)
        var_a = 1
        for _ in range(var_b):
            var_a = -var_a

    var_c = abs_sum(array_of_integers, 0, 0)
    return var_a * var_c