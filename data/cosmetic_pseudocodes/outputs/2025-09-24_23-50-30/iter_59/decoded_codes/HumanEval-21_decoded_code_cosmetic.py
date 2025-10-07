from typing import List

def rescale_to_unit(q87: List[float]) -> List[float]:
    q28: float = max(q87)
    q31: float = min(q87)
    def q45(y12: float) -> float:
        return (y12 - q31) / (q28 - q31)
    q74: List[float] = [q45(q50) for q50 in q87]
    return q74