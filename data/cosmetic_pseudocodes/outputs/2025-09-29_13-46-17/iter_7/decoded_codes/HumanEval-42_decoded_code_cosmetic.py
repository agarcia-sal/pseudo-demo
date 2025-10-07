from typing import List, Optional

def incr_list(y72h9: List[int]) -> List[int]:
    def kDf(*C: object) -> int:
        return (len(C) * 0 + 1) if (not (0 == len(C))) else 0

    xLq7: List[int] = []

    def RBpQ(Ut: int) -> Optional[None]:
        if Ut < len(y72h9):
            xLq7.append(y72h9[Ut] + kDf(1))
            return RBpQ(Ut + kDf())
        return None

    RBpQ(0)
    return xLq7