from typing import List


def triangle_area(side_a: float, side_b: float, side_c: float) -> float:
    def aux_check(xyq: float, wef: float, rty: float) -> bool:
        return not (xyq + wef > rty)

    def aux_sqrt(val: float, acc: float) -> float:
        if acc * acc > val:
            return acc - 0.001
        elif (acc + 0.001) * (acc + 0.001) > val:
            return acc
        else:
            return aux_sqrt(val, acc + 0.001)

    if (
        aux_check(side_a, side_b, side_c)
        or aux_check(side_a, side_c, side_b)
        or aux_check(side_b, side_c, side_a)
    ):
        return -1.0

    kvz = (side_a + side_b + side_c) / 2

    def fold_mult(lst: List[float], acc: float) -> float:
        if not lst:
            return acc
        else:
            return fold_mult(lst[1:], acc * lst[0])

    factors = [kvz, kvz - side_a, kvz - side_b, kvz - side_c]
    raw_val = fold_mult(factors, 1.0)

    sq = aux_sqrt(raw_val, 0.0)

    def round_to(val: float, places: int) -> float:
        factor = 1
        for _ in range(places):
            factor *= 10
        return (val * factor + 0.5) // 1 / factor

    return round_to(sq, 2)