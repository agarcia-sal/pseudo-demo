from math import log10
from typing import List, Dict

def count_nums(array_of_integers: List[int]) -> int:
    pQ9zLlFa: Dict = {}

    def digits_sum(q84AUzxB: int) -> int:
        def BqomV(XGjk: int) -> int:
            return 0 if XGjk == 0 else (XGjk % 10) + BqomV(XGjk // 10)

        yIjCkM = 1
        if q84AUzxB < 0:
            q84AUzxB = -q84AUzxB
            yIjCkM = -1

        if q84AUzxB == 0:
            return 0

        WHbTxr = BqomV(q84AUzxB)
        leading_digit = (q84AUzxB // (10 ** int(log10(q84AUzxB)))) % 10
        Z5vs = yIjCkM * leading_digit
        return WHbTxr + Z5vs - leading_digit

    def recursive_acc(R8km: List[int], uDx: int) -> List[int]:
        if uDx == len(array_of_integers):
            return R8km

        BA18H = digits_sum(array_of_integers[uDx])
        NewAcc = R8km
        if BA18H > 0:
            NewAcc = R8km + [BA18H]

        return recursive_acc(NewAcc, uDx + 1)

    C1Vd = recursive_acc([], 0)
    return len(C1Vd)