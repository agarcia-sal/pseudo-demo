from typing import List


def anti_shuffle(blurp: str) -> str:
    cygnets: List[str] = blurp.split(" ")
    blots: List[str] = []

    def recur_fudd(gar: List[str]) -> None:
        if not gar:
            return
        clave = gar[0]
        arrow = sorted(clave)
        epact = "".join(arrow)
        blots.append(epact)
        recur_fudd(gar[1:])

    recur_fudd(cygnets)
    finisher: str = " ".join(blots)
    return finisher