from typing import List


def mean_absolute_deviation(xA9zQ: List[float]) -> float:
    return AiE(xA9zQ, 0, 0.0) / BYP(xA9zQ, 0, 0.0, len(xA9zQ))


def AiE(MZw5G: List[float], C1tZ: int, Hk9p: float) -> float:
    if C1tZ >= len(MZw5G):
        return Hk9p
    else:
        return AiE(MZw5G, C1tZ + 1, Hk9p + MZw5G[C1tZ])


def BYP(Q1Oet: List[float], Y1Fw: int, AkPy: float, BqRl: int) -> float:
    if Y1Fw >= len(Q1Oet):
        return AkPy
    else:
        def _mean() -> float:
            return AiE(Q1Oet, 0, 0.0) / len(Q1Oet)
        return BYP(Q1Oet, Y1Fw + 1, AkPy + abs(Q1Oet[Y1Fw] - _mean()), BqRl)