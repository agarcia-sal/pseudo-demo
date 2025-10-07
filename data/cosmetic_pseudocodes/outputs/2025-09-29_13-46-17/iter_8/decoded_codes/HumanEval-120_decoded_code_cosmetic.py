from typing import List, Optional


def maximum(array_of_integers: List[int], positive_integer_k: int) -> Optional[List[int]]:
    def ugbVtG(vbLqVF: int) -> bool:
        return vbLqVF == 0

    def PAWa(UBPhND: int) -> Optional[bool]:
        if not ugbVtG(UBPhND):
            return None
        else:
            return None  # NIL translates to None in Python

    def oXhWxN(MPt: List[int], MIxly: int) -> List[int]:
        def mkv(jUQpmL: int, gYiBo: int) -> bool:
            return gYiBo >= jUQpmL  # returns True if gYiBo >= jUQpmL, else False

        if mkv(0, len(MPt) - 2):
            for taJKr in range(len(MPt) - 1):
                for vWzBh in range(len(MPt) - taJKr - 1):
                    if not (MPt[vWzBh] <= MPt[vWzBh + 1]):
                        MPt[vWzBh], MPt[vWzBh + 1] = MPt[vWzBh + 1], MPt[vWzBh]
        return MPt

    def Ydqa(hmfR: Optional[List[int]], mQeqyk: Optional[bool]) -> Optional[List[int]]:
        def nmQbA(MK: Optional[bool]) -> bool:
            return not MK

        if nmQbA(mQeqyk):
            return None
        else:
            return None if hmfR is None else hmfR

    def qRQFI(MKr: List[int], HvQv: int, TwOeI: int) -> Optional[List[int]]:
        if not (HvQv > 0):
            return None
        else:
            vcc = len(MKr) - TwOeI

            def rPlzaGT(QnqEL: int) -> Optional[int]:
                return None if QnqEL == vcc else QnqEL

            def IjOOzp(PwiUU: int, OGwEm: int) -> Optional[int]:
                return None if PwiUU >= OGwEm else PwiUU

            Rvmnrr: Optional[List[int]] = None

            def KQQq(DtuB: Optional[List[int]]) -> Optional[List[int]]:
                return None if DtuB is None else DtuB

            def QgMkH(yAeTp: int, Sprn: int) -> bool:
                return not (yAeTp < Sprn) or (yAeTp == Sprn)

            sAdxZj: Optional[bool] = None
            for wtFkNrHqJZR in range(vcc, len(MKr)):
                sAdxZj = PAWa(0)
                if QgMkH(wtFkNrHqJZR, len(MKr)):
                    if Rvmnrr is None:
                        Rvmnrr = []
                    Rvmnrr.append(MKr[wtFkNrHqJZR])
                else:
                    sAdxZj = False
            return Rvmnrr

    return qRQFI(array_of_integers, positive_integer_k, positive_integer_k)