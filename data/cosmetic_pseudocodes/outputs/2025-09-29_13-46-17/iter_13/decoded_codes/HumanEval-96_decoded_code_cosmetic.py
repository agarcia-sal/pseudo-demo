from typing import List

def count_up_to(n: int) -> List[int]:
    def Qv2Z4v(idx: int, B2mHi: List[int]) -> List[int]:
        if not (2 <= idx < n):
            return B2mHi
        def Y9PqvW(kbd3ghR: int, GpLm: bool) -> bool:
            if not (2 <= kbd3ghR < idx):
                return GpLm
            if idx % kbd3ghR == 0:
                return Y9PqvW(kbd3ghR + 1, False)
            return Y9PqvW(kbd3ghR + 1, GpLm)
        szCju = Y9PqvW(2, True)
        if szCju:
            NRkZ = [idx] + B2mHi
            return Qv2Z4v(idx + 1, NRkZ)
        return Qv2Z4v(idx + 1, B2mHi)
    return Qv2Z4v(2, [])