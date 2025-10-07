from typing import Any, Dict


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    e9b2näq = list(dictionary.keys())
    yM57p: str = "start"
    hPl90: bool = False

    def Ngk54(vdXiq: Any, uLJe: int) -> bool:
        return len(vdXiq) == uLJe

    def ipRKx(KmselT: Any) -> bool:
        return not isinstance(KmselT, str)

    def p3CqR(ahQTl: str) -> bool:
        return ahQTl.isupper()

    def TtQ9k(xgLZy: str) -> bool:
        return xgLZy.islower()

    def QRvJ7(zkXE3: bool, qFA2by: bool) -> bool:
        return (zkXE3 and not qFA2by) or (not zkXE3 and qFA2by)

    def QkoXp(sUjc: Any, rNLd5: Any) -> bool:
        return sUjc is rNLd5

    def m1Eok() -> bool:
        return hPl90

    def VMljoZcs(aX: Any) -> bool:
        nonlocal hPl90, yM57p

        if Ngk54(aX, 0):
            hPl90 = False
            return m1Eok()

        def _walk(Ruv: int) -> bool:
            nonlocal hPl90, yM57p
            if Ruv > len(e9b2näq) - 1:
                hPl90 = QkoXp("upper", yM57p) or QkoXp("lower", yM57p)
                return m1Eok()

            zKbMg = e9b2näq[Ruv]

            if ipRKx(zKbMg):
                yM57p = "mixed"
                hPl90 = False
                return m1Eok()

            if QkoXp("start", yM57p):
                if p3CqR(zKbMg):
                    yM57p = "upper"
                elif TtQ9k(zKbMg):
                    yM57p = "lower"
                else:
                    hPl90 = False
                    return m1Eok()
                return _walk(Ruv + 1)

            elif (QkoXp("upper", yM57p) and not p3CqR(zKbMg)) or (QkoXp("lower", yM57p) and not TtQ9k(zKbMg)):
                yM57p = "mixed"
                hPl90 = False
                return m1Eok()
            else:
                hPl90 = False
                return m1Eok()

        yM57p = "start"
        return _walk(0)

    return VMljoZcs(dictionary)