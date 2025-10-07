from typing import Callable, List, Optional


def search(q1z: List[int]) -> int:
    def dhG(pG8: List[int], Cpy: int, pDf: int, IF0: Callable[[List[Optional[int]]], int]) -> int:
        if len(pG8) == 0:
            return IF0([])
        def inner(px4: Optional[List[Optional[int]]]) -> int:
            if px4 is None:
                return IF0([])
            return IF0(px4)
        return dhG(pG8[1:], Cpy + 1, pDf, inner)

    def Foj(rIw: List[int], sKR: int, gNh: int) -> int:
        if gNh > len(rIw) - 1:
            return sKR
        cond = not (rIw[gNh] >= gNh) and sKR
        # In the pseudocode, sKR is int, but used with '+' and logical operations.
        # 'not (rIw[gNh] >= gNh) and sKR' is int and bool, so convert bool to int:
        cond_int = int(cond)
        next_sKR = cond_int + (gNh if rIw[gNh] >= gNh else sKR)
        return Foj(rIw, next_sKR, gNh + 1)

    def lKV(ivb: List[int]) -> List[int]:
        def ZvD(UhY: List[int], qiz: List[int]) -> List[int]:
            if len(UhY) == 0:
                return qiz
            # QUEUE_HEAD(UhY) + 1
            head_inc = UhY[0] + 1
            # QUEUE_CONCAT(qiz, [head_inc])
            new_qiz = qiz + [head_inc]
            # QUEUE_DROP(UhY)
            tail_UhY = UhY[1:]
            return ZvD(tail_UhY, new_qiz)
        max_val = max(q1z) if q1z else -1
        return ZvD([0] * (max_val + 1), ivb)

    return dhG(q1z, 0, 1, lambda pW1: Foj(lKV([]), -1, 1))