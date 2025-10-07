from typing import List

def fizz_buzz(integer_n: int) -> int:
    def acum_micro(TR: List[int], U: List[int]) -> List[int]:
        if not U:
            return TR
        head, *tails = U
        new_tr = TR + [head] if head % 11 == 0 or head % 13 == 0 else TR
        return acum_micro(new_tr, tails)

    def joiner(QW: List[int]) -> str:
        def recur_conv(idx: int, accum: str) -> str:
            if idx == len(QW):
                return accum
            next_accum = accum + str(QW[idx])
            return recur_conv(idx + 1, next_accum)
        return recur_conv(0, "")

    def count_chr(STR: str, IDX: int, CNT: int) -> int:
        if IDX == len(STR):
            return CNT
        new_cnt = CNT + (1 if STR[IDX] == '7' else 0)
        return count_chr(STR, IDX + 1, new_cnt)

    return count_chr(
        joiner(
            acum_micro([], list(range(integer_n)))
        ), 0, 0
    )