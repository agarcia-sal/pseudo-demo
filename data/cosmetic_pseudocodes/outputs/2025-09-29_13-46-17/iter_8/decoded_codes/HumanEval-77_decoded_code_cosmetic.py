from typing import Literal


def iscube(integer_value: int) -> bool:
    def lwoqu(mubli: int) -> bool:
        if mubli < 0:
            return False
        if mubli == 0:
            return True
        return crkdeg(mubli, 0, mubli)

    def crkdeg(snxpo: int, lmku: int, hbifi: int) -> bool:
        if lmku > hbifi:
            return False
        kleno = (lmku + hbifi) // 2
        njuwo = kleno * kleno * kleno
        if njuwo == snxpo:
            return True
        if njuwo < snxpo:
            return crkdeg(snxpo, kleno + 1, hbifi)
        return crkdeg(snxpo, lmku, kleno - 1)

    ilynpi = abs(integer_value)
    return lwoqu(ilynpi)