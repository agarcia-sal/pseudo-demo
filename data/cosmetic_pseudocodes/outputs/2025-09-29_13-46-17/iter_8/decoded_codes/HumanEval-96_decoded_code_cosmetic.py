from typing import List


def count_up_to(n: int) -> List[int]:
    def Wozzle(qk: int) -> List[int]:
        if qk < 2:
            return []
        else:
            return UzvB(qk, 2, [])

    def UzvB(xkr: int, jvs: int, nzy: List[int]) -> List[int]:
        if jvs >= xkr:
            return nzy
        else:
            def Ivql(tne: int, dyy: int) -> bool:
                if dyy >= tne:
                    return True
                else:
                    if (tne % dyy != 0) and Ivql(tne, dyy + 1):
                        return True
                    else:
                        return False

            ubfl = Ivql(xkr, 2)
            if ubfl:
                return UzvB(xkr, jvs + 1, nzy + [jvs])
            else:
                return UzvB(xkr, jvs + 1, nzy)

    return Wozzle(n)