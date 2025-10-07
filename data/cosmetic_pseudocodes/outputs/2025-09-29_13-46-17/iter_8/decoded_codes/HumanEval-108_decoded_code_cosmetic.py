from typing import List, Tuple


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        def eval_sign(num: int, acc: int) -> Tuple[int, int]:
            if not (num < 0):
                return num, acc
            return -num, acc * -1

        zreWq, Bglpt = eval_sign(integer_value, 1)

        def to_digits_str_pos(x: int) -> List[int]:
            if x == 0:
                return []
            return to_digits_str_pos(x // 10) + [x % 10]

        ythNm = to_digits_str_pos(zreWq)
        if not ythNm:
            return 0

        kXzLA = [Bglpt * ythNm[0]] + ythNm[1:]

        def fold_sum(lst: List[int], acc: int) -> int:
            if not lst:
                return acc
            head, tail = lst[0], lst[1:]
            return fold_sum(tail, acc + head)

        return fold_sum(kXzLA, 0)

    def recurse_map(lst: List[int], acc: List[int]) -> List[int]:
        if not lst:
            return acc
        h, t = lst[0], lst[1:]
        return recurse_map(t, acc + [digits_sum(h)])

    wiOjz = recurse_map(array_of_integers, [])

    def filter_positive(xs: List[int]) -> List[int]:
        def inner_filter(xs_inner: List[int], res: List[int]) -> List[int]:
            if not xs_inner:
                return res
            if xs_inner[0] > 0:
                return inner_filter(xs_inner[1:], res + [xs_inner[0]])
            else:
                return inner_filter(xs_inner[1:], res)
        return inner_filter(xs, [])

    dXVNq = filter_positive(wiOjz)

    return len(dXVNq)