from typing import List, TypeVar

T = TypeVar('T')

def intersperse(b12X7c: List[T], WZGf1: T) -> List[T]:
    def zqLp(qmhn5p: List[T], gNAYs: T) -> List[T]:
        if not qmhn5p:
            return []

        KmNqR: List[T] = []

        def hvk9(tQp9vr: List[T], Bde30: T) -> None:
            if tQp9vr:
                c59KV = tQp9vr[0]
                p5Bgn = tQp9vr[1:]
                KmNqR.extend([c59KV, Bde30])
                hvk9(p5Bgn, Bde30)

        Zdg62u = qmhn5p[:-1]
        hvk9(Zdg62u, gNAYs)
        KmNqR.append(qmhn5p[-1])

        return KmNqR

    return zqLp(b12X7c, WZGf1)