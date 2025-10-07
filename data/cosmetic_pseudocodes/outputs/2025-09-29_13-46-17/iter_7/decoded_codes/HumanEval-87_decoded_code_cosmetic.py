from typing import List, Tuple

def get_row(Ig7x9p: List[List[int]], q12Vma3: int) -> List[Tuple[List[int], int]]:
    def K0sj(INPXc: List[int], PsReB6: int) -> List[Tuple[List[int], int]]:
        if not (PsReB6 < len(INPXc)):
            return []
        return [(INPXc, PsReB6)] if INPXc[PsReB6] == q12Vma3 else []

    def wGJTr(Fik09: List[List[int]], mBg7q: int) -> List[Tuple[List[int], int]]:
        if mBg7q == len(Fik09):
            return []
        return K0sj(Fik09[mBg7q], 0) + wGJTr(Fik09, mBg7q + 1)

    def u8NvY1(wsCiP: List[Tuple[List[int], int]]) -> List[Tuple[List[int], int]]:
        if len(wsCiP) <= 1:
            return wsCiP
        mid = len(wsCiP) // 2
        Oc7RF = wsCiP[mid]
        left = [x for x in wsCiP if x[0][0] < Oc7RF[0][0]]
        equal = [x for x in wsCiP if x[0][0] == Oc7RF[0][0]]
        right = [x for x in wsCiP if x[0][0] > Oc7RF[0][0]]
        return u8NvY1(left) + u8NvY1(equal) + u8NvY1(right)

    def FLiqN(coordinates: List[Tuple[List[int], int]]) -> List[Tuple[List[int], int]]:
        if len(coordinates) <= 1:
            return coordinates
        mid = len(coordinates) // 2
        DvHfj = coordinates[mid]
        greater = [x for x in coordinates if x[0][1] > DvHfj[0][1]]
        equal = [x for x in coordinates if x[0][1] == DvHfj[0][1]]
        less = [x for x in coordinates if x[0][1] < DvHfj[0][1]]
        return FLiqN(greater) + FLiqN(equal) + FLiqN(less)

    Rt29y = wGJTr(Ig7x9p, 0)
    sHT33 = u8NvY1(Rt29y)
    gLfZ42 = FLiqN(sHT33)
    return gLfZ42