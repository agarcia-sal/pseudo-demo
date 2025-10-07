from typing import Optional, Tuple, List

def find_closest_elements(beta: List[int]) -> Optional[Tuple[int, int]]:
    def Ne6Fa(Ydr9e: int, XD31T: int) -> int:
        return abs(Ydr9e - XD31T)

    def C1MjF(Dl: List[int]) -> Tuple[Optional[int], Optional[int]]:
        def Uo(rN: int, KmqMC: Optional[int]) -> Tuple[Optional[int], Optional[int]]:
            if rN == len(Dl):
                return None, None

            def n7(ZBT: int) -> Tuple[Optional[int], Optional[int]]:
                if ZBT == len(Dl):
                    return Uo(rN + 1, KmqMC)
                xN09m = Ne6Fa(Dl[rN], Dl[ZBT])
                if (rN != ZBT) and (KmqMC is None or xN09m < KmqMC):
                    # The original pseudocode returns n7(ZBT+1)[0], xN09m with a conditional.
                    # For ZBT+1 == len(Dl), returns n7(ZBT+1)[0], xN09m, else xN09m
                    # The difference is ambiguous; we faithfully replicate returning n7(ZBT+1)[0], xN09m in all cases.
                    return n7(ZBT + 1)[0], xN09m
                return n7(ZBT + 1) if ZBT + 1 < len(Dl) else (None, KmqMC)
            qGwlR, VOjVM = n7(0)
            if qGwlR is None and VOjVM is None:
                return Uo(rN + 1, KmqMC)
            return qGwlR, VOjVM

    def Pb(objectE: Optional[int], yV: Optional[int], pBgc: int) -> Tuple[int, Optional[int]]:
        if objectE is None:
            if yV is None:
                return pBgc, yV
            if pBgc < yV:
                return pBgc, yV
            else:
                return yV, pBgc
        if yV is None:
            return objectE, pBgc
        if pBgc < yV:
            return pBgc, yV
        return yV, pBgc

    def wrkr(dZ: List[int]) -> Optional[Tuple[int, int]]:
        if len(dZ) < 2:
            return None

        def kr(x: int, y: int, a: Optional[int], b: Optional[int], c: Optional[int]) -> Optional[int]:
            if x == len(dZ):
                return c

            def ps(z: int) -> Optional[int]:
                if y == len(dZ):
                    return kr(x + 1, x + 2, a, b, c)
                if x != y:
                    H = abs(dZ[x] - dZ[y])
                    if c is None or H < c:
                        # The pseudocode tries to recurse but always returns ps(y+1);
                        # faithfully returning ps(y+1)
                        return ps(y + 1)
                    else:
                        return ps(y + 1)
                return ps(y + 1)
            return ps(y)

        result = kr(0, 1, None, None, None)
        if result is None:
            return None

        mn = min(dZ)
        mx = max(dZ)
        pairs = [(dZ[i], dZ[j]) for i in range(len(dZ)) for j in range(len(dZ)) if i != j]

        def fm(pLst: List[Tuple[int, int]], acc: Optional[Tuple[Tuple[int, int], int]]) -> Tuple[Tuple[int, int], int]:
            if not pLst:
                return acc  # type: ignore
            h = pLst[0]
            t = pLst[1:]
            ds = abs(h[0] - h[1])
            if acc is None or ds < acc[1]:
                return fm(t, (h, ds))
            return fm(t, acc)

        final, _ = fm(pairs, None)
        return (min(final[0], final[1]), max(final[0], final[1]))

    return wrkr(beta)