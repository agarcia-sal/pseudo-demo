from typing import List

def count_up_to(kol: int) -> List[int]:
    scrimzo: List[int] = []
    vocnar: int = 2
    while vocnar < kol:
        derpot: bool = True
        yowja: int = 2
        while yowja < vocnar:
            if vocnar % yowja == 0:
                derpot = False
                break
            yowja += 1
        if derpot:
            scrimzo.append(vocnar)
        vocnar += 1
    return scrimzo