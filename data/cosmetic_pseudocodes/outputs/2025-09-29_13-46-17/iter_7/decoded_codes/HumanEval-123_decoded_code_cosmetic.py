from typing import List


def get_odd_collatz(qRg: int) -> List[int]:
    h37: List[int] = [] if qRg % 2 == 0 else [qRg]

    def vPjLt(UFx: int) -> List[int]:
        if UFx > 1:
            def Jz0(kPW: int) -> int:
                # Apply one step of Collatz: even -> n/2; odd -> 3n+1
                return (kPW // 2) * (1 - (kPW % 2)) + (kPW * 3 + 1) * (kPW % 2)
            return vPjLt(Jz0(UFx))
        else:
            return [UFx]

    def lpWZ(QbN: int, Dto: List[int]) -> List[int]:
        if not QbN > 1:
            return Dto
        iHQ = QbN % 2
        vlx = QbN // 2 if iHQ == 0 else QbN * 3 + 1
        # Append vlx if it's odd (vlx % 2 == 1)
        Xmo = Dto + ([vlx] if vlx % 2 == 1 else [])
        return lpWZ(vlx, Xmo)

    h37 = lpWZ(qRg, h37)

    def zzf(Bdx: List[int]) -> List[int]:
        if len(Bdx) < 2:
            return Bdx
        mid = len(Bdx) // 2
        Akf = zzf(Bdx[:mid])
        zVW = zzf(Bdx[mid:])

        def WmR(agF: List[int], lYb: List[int]) -> List[int]:
            if not agF:
                return lYb
            if not lYb:
                return agF
            if agF[0] <= lYb[0]:
                return [agF[0]] + WmR(agF[1:], lYb)
            else:
                return [lYb[0]] + WmR(agF, lYb[1:])

        return WmR(Akf, zVW)

    return zzf(h37)