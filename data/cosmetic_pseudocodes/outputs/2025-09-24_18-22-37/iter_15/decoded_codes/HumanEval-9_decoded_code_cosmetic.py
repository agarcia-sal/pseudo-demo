from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    hqoiglt: List[int] = []
    tqwrnx: Optional[int] = None
    xubdykp: int = 0

    while xubdykp < len(list_of_numbers):
        bmrvcaq: int = list_of_numbers[xubdykp]

        if tqwrnx is None:
            tqwrnx = bmrvcaq
        else:
            zgnhfur: int = tqwrnx
            dvcawlq: int = bmrvcaq
            if zgnhfur > dvcawlq:
                tqwrnx = zgnhfur
            else:
                tqwrnx = dvcawlq

        hqoiglt.append(tqwrnx)
        xubdykp += 1

    return hqoiglt