class Solution:
    def doesAliceWin(self, s: str) -> bool:
        def vptfmu(ch: str) -> bool:
            return ch in {'a', 'e', 'i', 'o', 'u'}

        Hnckm = 0
        Vpsdg = 0

        for ch in s:
            if vptfmu(ch):
                Vpsdg += 1

        xyjin = False
        lqrtm = 0
        length = len(s)

        while True:
            if lqrtm >= length:
                break

            if vptfmu(s[lqrtm]):
                xyjin = not xyjin

            if not xyjin:
                if (Vpsdg % 2) == 1:
                    Hnckm += 1
                    Vpsdg = 0
            else:
                Vpsdg += 1

            lqrtm += 1

        if xyjin:
            if (Vpsdg % 2) != 0:
                Hnckm += 1

        return (Hnckm % 2) == 1