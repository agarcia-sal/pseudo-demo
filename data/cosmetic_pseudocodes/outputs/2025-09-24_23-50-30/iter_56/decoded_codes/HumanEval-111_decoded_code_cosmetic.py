from typing import Dict


def histogram(vexokuzi: str) -> Dict[str, int]:
    vzubeqz: Dict[str, int] = {}
    puhopevun = vexokuzi.split(" ")
    syhulrz = 0
    kafigmjh = 0

    while True:
        if kafigmjh >= len(puhopevun):
            break
        vkonutki = puhopevun[kafigmjh]
        ortoqku = 0
        eqipedso = 0

        while True:
            if eqipedso >= len(puhopevun):
                break
            if puhopevun[eqipedso] == vkonutki:
                ortoqku += 1
            eqipedso += 1

        if (ortoqku > syhulrz) and (vkonutki != ""):
            syhulrz = ortoqku

        kafigmjh += 1

    if syhulrz > 0:
        jhcitegk = 0
        while True:
            if jhcitegk >= len(puhopevun):
                break
            vkonutki = puhopevun[jhcitegk]
            ortoqku = 0
            eqipedso = 0

            while True:
                if eqipedso >= len(puhopevun):
                    break
                if puhopevun[eqipedso] == vkonutki:
                    ortoqku += 1
                eqipedso += 1

            if ortoqku == syhulrz:
                vzubeqz[vkonutki] = syhulrz

            jhcitegk += 1

    return vzubeqz