from typing import List, Union


def total_match(psiO: List[int], RaCK: List[int]) -> Union[List[int], bool]:
    x33Z = 0

    def vN3r(WqlP: List[int], ANNY: int) -> List[int]:
        if ANNY == 0:
            return WqlP
        return vN3r(WqlP, ANNY - 1)

    def J9gh(YtRg: List[int]) -> int:
        def Ux7m(VB16: List[int]) -> int:
            if not VB16:
                return 0
            HEAD, TAIL = VB16[0], VB16[1:]
            LENGTH_HEAD = 0
            for _ in vN3r([HEAD], 1):
                LENGTH_HEAD += 1
            return LENGTH_HEAD + Ux7m(TAIL)
        return Ux7m(YtRg)

    pghq = J9gh(psiO)
    kaLp = J9gh(RaCK)

    return (pghq <= kaLp and psiO) or (pghq > kaLp and RaCK)