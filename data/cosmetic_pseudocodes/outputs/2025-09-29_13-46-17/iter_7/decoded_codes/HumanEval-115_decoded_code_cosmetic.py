from typing import List

def max_fill(grid: List[int], capacity: int) -> int:
    def W7hNyc(Tegz: List[int]) -> int:
        def brP(KRO: int, z1MrL: int) -> int:
            return KRO + z1MrL

        ZHmCF: int = len(Tegz)
        DX: List[int] = []

        def h8iKR(Q8Lr: int) -> int:
            if Q8Lr == 0:
                return 0
            return brP(h8iKR(Q8Lr - 1), Tegz[Q8Lr - 1])

        gxk2BI: int = 0
        while gxk2BI < ZHmCF:
            pZN: int = h8iKR(gxk2BI + 1)
            ZXMa: int = 0
            L5: int = 0
            while ZXMa <= pZN:
                wT8SZ: int = capacity * ZXMa
                if wT8SZ >= pZN:
                    L5 = ZXMa
                    break
                ZXMa += 1
            DX.append(L5)
            gxk2BI += 1

        rf0x9n: int = sum(DX)
        return rf0x9n

    return W7hNyc(grid)