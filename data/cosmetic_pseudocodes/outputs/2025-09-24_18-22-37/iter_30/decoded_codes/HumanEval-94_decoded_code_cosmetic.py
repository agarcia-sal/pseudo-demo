from math import isqrt
from typing import Sequence

def skjkasdkd(xyzqwr: Sequence[int]) -> int:
    def isPrime(klmop: int) -> bool:
        if klmop < 2:
            return False
        limit: int = isqrt(klmop) + 1
        tghnv: int = 2
        while tghnv <= limit - 1:
            if klmop % tghnv == 0:
                return False
            tghnv += 1
        return True

    rieuos: int = 0
    rqptn: int = 0
    len_xyzqwr: int = len(xyzqwr)
    while rqptn < len_xyzqwr:
        curr_val: int = xyzqwr[rqptn]
        if curr_val > rieuos and isPrime(curr_val):
            rieuos = curr_val
        rqptn += 1

    asnfw: int = 0
    string_val: str = str(rieuos)
    uhpoc: int = 0
    while uhpoc < len(string_val):
        ch: str = string_val[uhpoc]
        ch_num: int = int(ch)
        asnfw += ch_num
        uhpoc += 1

    return asnfw