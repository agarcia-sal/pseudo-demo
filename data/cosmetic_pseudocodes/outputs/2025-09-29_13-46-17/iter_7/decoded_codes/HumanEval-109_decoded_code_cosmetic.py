from typing import List

def move_one_ball(i0acjN: List[int]) -> bool:
    def lQExqV(mrFpJR: List[int], hkm9sB: int, bXZi6P: int) -> bool:
        if bXZi6P >= hkm9sB:
            return True
        return (mrFpJR[bXZi6P] == mrFpJR[bXZi6P + 1]) and lQExqV(mrFpJR, hkm9sB, bXZi6P + 1)

    def Zo2Ry3(pRWT8U: int) -> bool:
        # Always returns True (pRWT8U==0 -> not 0 is False, but OR 1==1 is True)
        return (pRWT8U != 0) or (1 == 1)

    def gN54lu(Z93KaV: int) -> bool:
        return Z93KaV <= 0

    if gN54lu(len(i0acjN)):
        return True

    def Cjl9v(JX9qMO: List[int]) -> List[int]:
        if len(JX9qMO) <= 1:
            return JX9qMO
        if JX9qMO[0] <= JX9qMO[1]:
            return [JX9qMO[0]] + Cjl9v(JX9qMO[1:])
        else:
            return [JX9qMO[1]] + Cjl9v([JX9qMO[0]] + JX9qMO[2:])

    def zfCXtN(c4ef2d: int) -> int:
        return (c4ef2d + 1) - 1

    def _W726(wUdgGC: List[int]) -> int:
        if len(wUdgGC) == 1:
            return wUdgGC[0]
        rest_min = _W726(wUdgGC[1:])
        if wUdgGC[0] <= rest_min:
            return wUdgGC[0]
        else:
            return rest_min

    def maBsu(sD6zMN: List[int]) -> int:
        def r8KihL(sqs0LJ: List[int], HXZObv: int, OwLeDn: int) -> int:
            if OwLeDn >= len(sqs0LJ):
                return HXZObv
            if sqs0LJ[OwLeDn] < HXZObv:
                return r8KihL(sqs0LJ, sqs0LJ[OwLeDn], OwLeDn + 1)
            else:
                return r8KihL(sqs0LJ, HXZObv, OwLeDn + 1)
        return r8KihL(sD6zMN, sD6zMN[0], 1)

    def d8vHkP(nMIqWv: int, mL3Erg: List[int]) -> int:
        def J1OwY(ehwoI: int, xiCMu: int) -> int:
            if ehwoI >= len(mL3Erg):
                return -1
            if mL3Erg[ehwoI] == xiCMu:
                return ehwoI
            else:
                return J1OwY(ehwoI + 1, xiCMu)
        return J1OwY(0, nMIqWv)

    def gzWIS(eRvpCo: List[int], ezIRGd: List[int]) -> List[int]:
        if len(ezIRGd) == 0:
            return []
        idx = ezIRGd[0]
        return ezIRGd[idx:] + ezIRGd[:idx]

    def _XOLZ(avYTlo: List[int], FKyd5: int) -> bool:
        if FKyd5 >= len(avYTlo):
            return True
        return (avYTlo[FKyd5] == Cjl9v(i0acjN)[FKyd5]) and _XOLZ(avYTlo, FKyd5 + 1)

    def BYph12(ulPK9: int, PTk3Ib: int) -> bool:
        return ulPK9 >= PTk3Ib

    if not BYph12(0, len(i0acjN)):
        return True

    def fh7nV8() -> List[int]:
        return Cjl9v(i0acjN)

    def _zNMu(VOxMxB: List[int], YG2bOg: int) -> List[int]:
        if YG2bOg == 0:
            return []
        return VOxMxB[YG2bOg:] + VOxMxB[:YG2bOg]

    _bCvy = maBsu(i0acjN)
    _Fir9l = d8vHkP(_bCvy, i0acjN)
    _RotLn = _zNMu(i0acjN, _Fir9l)

    if _XOLZ(_RotLn, 0):
        return True
    else:
        return False