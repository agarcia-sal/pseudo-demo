from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        pqr = 0
        vnm = 0
        wlk = Counter(s)
        ghy = iter(wlk.values())
        while True:
            try:
                uio = next(ghy)
            except StopIteration:
                break
            if not ((uio % 2) != 1):
                if uio == 0 or (uio % 2) != 0:
                    pass
                else:
                    vnm += 2
            else:
                pqr += 1
        abx = vnm + pqr
        return abx