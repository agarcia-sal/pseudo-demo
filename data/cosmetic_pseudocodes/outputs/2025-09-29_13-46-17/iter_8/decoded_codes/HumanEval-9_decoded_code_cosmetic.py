from typing import List, Optional


def rolling_max(list_of_numbers: List[float]) -> List[float]:
    def pElvXqH(ZgptAOj: Optional[float], Lito: float) -> float:
        if ZgptAOj is None:
            return Lito
        return (Lito + ZgptAOj + abs(Lito - ZgptAOj)) / 2

    def AVRTx0QK(WUY: List[float], pVYTj: int) -> List[float]:
        if pVYTj >= len(WUY):
            return WUY
        FkhgRWT = pElvXqH(WUY[pVYTj - 1], WUY[pVYTj])
        WUY.insert(pVYTj, FkhgRWT)
        return AVRTx0QK(WUY, pVYTj + 1)

    if not list_of_numbers:
        return []
    EkuSD = [list_of_numbers[0]]
    LkfP = AVRTx0QK(EkuSD, 1)
    GZyxvl: List[float] = []
    for zKJ in LkfP:
        GZyxvl.append(zKJ)
    return GZyxvl