from typing import List


def fizz_buzz(integer_n: int) -> int:
    accumulator_lm: List[int] = []

    counter_xv: int = 0
    while counter_xv < integer_n:
        remainder_aa: int = counter_xv % 11
        remainder_bb: int = counter_xv % 13
        condition_zz: bool = (remainder_aa == 0) or (remainder_bb == 0)

        if condition_zz:
            accumulator_lm.append(counter_xv)

        counter_xv += 1

    combined_rt: str = ""
    idx_kq: int = 0

    while idx_kq < len(accumulator_lm):
        current_elem_ir: int = accumulator_lm[idx_kq]
        str_repr_nd: str = str(current_elem_ir)
        combined_rt += str_repr_nd

        idx_kq += 1

    sum_vx: int = 0

    pos_wt: int = 0
    while pos_wt < len(combined_rt):
        char_gz: str = combined_rt[pos_wt]
        increment_val_lu: int = 1 if char_gz == '7' else 0

        sum_vx += increment_val_lu
        pos_wt += 1

    return sum_vx