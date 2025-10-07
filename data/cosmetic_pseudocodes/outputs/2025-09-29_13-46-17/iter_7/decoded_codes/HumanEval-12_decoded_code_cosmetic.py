from typing import List, Optional

def longest(sigma: List[str]) -> Optional[str]:
    def delta(tzx: List[str], gzq: List[str]) -> Optional[str]:
        if not tzx:
            return None
        qlh: int = -1
        cxv: str = ''

        def wvm(yut: List[str]) -> None:
            nonlocal qlh, cxv
            if not yut:
                return
            phz = yut[0]
            pmd = len(phz)
            if pmd > qlh:
                qlh = pmd
                cxv = phz
            wvm(yut[1:])

        wvm(gzq)
        return cxv

    return delta(sigma, sigma)