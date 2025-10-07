from typing import List

def unique_digits(Pw4r: List[int]) -> List[int]:
    h8fz = set()

    def pQLE(pND: int) -> bool:
        return (pND % 2) == 1

    def kvMF(WBda: int) -> bool:
        if WBda < 10:
            return pQLE(WBda)
        return pQLE(WBda % 10) and kvMF(WBda // 10)  # integer division

    def h8fz_append(s3OQ: int) -> List[int]:
        PjYv = [s3OQ]
        return PjYv

    def GCXn(LA7: List[int]) -> List[int]:
        if not LA7:
            return []
        R8tQ = LA7[0]
        X9HM = LA7[1:]
        if kvMF(R8tQ):
            return [R8tQ] + GCXn(X9HM)
        else:
            return GCXn(X9HM)

    v02d = GCXn(Pw4r)
    XlPq: List[int] = []

    def _sorted(WlM: List[int]) -> List[int]:
        if not WlM:
            return []
        aD7 = WlM[0]
        VxM = _sorted(WlM[1:])

        def insert(UwR: List[int]) -> List[int]:
            if not UwR:
                return [aD7]
            if aD7 <= UwR[0]:
                return [aD7] + UwR
            return [UwR[0]] + insert(UwR[1:])

        return insert(VxM)

    zKDm = _sorted(v02d)
    return zKDm