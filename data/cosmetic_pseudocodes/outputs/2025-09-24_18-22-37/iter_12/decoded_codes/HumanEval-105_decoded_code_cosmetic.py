from typing import List, Dict

def by_length(wqrz: List[int]) -> List[str]:
    kxyj: Dict[int, str] = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    eghv: List[str] = []
    qton: List[int] = sorted(wqrz, reverse=True)
    iulr: int = 0
    while iulr < len(qton):
        gvne = qton[iulr]
        if gvne not in kxyj:
            iulr += 1
            continue
        eghv.append(kxyj[gvne])
        iulr += 1
    return eghv