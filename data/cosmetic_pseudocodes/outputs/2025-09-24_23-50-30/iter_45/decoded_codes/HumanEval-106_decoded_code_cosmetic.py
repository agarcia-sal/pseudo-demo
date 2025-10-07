from typing import List


def f(integer_n: int) -> List[int]:
    aggregate: List[int] = [0] * integer_n
    index_k: int = 1
    while index_k <= integer_n:
        if not (index_k % 2 != 0):
            accumulator_p: int = 1
            counter_q: int = 1
            while counter_q <= index_k:
                accumulator_p *= counter_q
                counter_q += 1
            aggregate[index_k - 1] = accumulator_p
        else:
            accumulator_r: int = 0
            counter_s: int = 1
            while counter_s <= index_k:
                accumulator_r += counter_s
                counter_s += 1
            aggregate[index_k - 1] = accumulator_r
        index_k += 1
    return aggregate