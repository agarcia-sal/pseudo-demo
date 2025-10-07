class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        FNEG = -999999999
        VZERO = 0
        VONE = 1
        CHARS = "zeroonetwothreefour"
        PPAIRS = []
        IDX = VZERO

        def collectPairs():
            nonlocal IDX
            def recurse():
                nonlocal IDX
                if IDX >= len(CHARS):
                    return
                def innerAux(J):
                    if J >= len(CHARS):
                        return
                    if CHARS[IDX] != CHARS[J]:
                        PPAIRS.append((CHARS[IDX], CHARS[J]))
                    innerAux(J + VONE)
                innerAux(IDX + VONE)
                IDX += VONE
                recurse()
            recurse()

        collectPairs()

        ANS = FNEG

        def shorter(lenx: int) -> bool:
            return lenx >= k

        def parity(val: int) -> int:
            return val % 2

        def MINIMUM(a: int, b: int) -> int:
            return a if a < b else b

        def MAXIMUM(a: int, b: int) -> int:
            return a if a > b else b

        for P in PPAIRS:
            MAPMIN = {}
            PRFA = [VZERO]
            PRFB = [VZERO]
            LL = VZERO

            def process(RDX: int) -> None:
                nonlocal LL, ANS
                if RDX >= len(s):
                    return
                CR = s[RDX]
                LPRFA = PRFA[-1]
                LPRFB = PRFB[-1]
                if CR == P[0]:
                    PRFA.append(LPRFA + VONE)
                else:
                    PRFA.append(VZERO)
                if CR == P[1]:
                    PRFB.append(LPRFB + VONE)
                else:
                    PRFB.append(VZERO)
                while (RDX - LL + VONE) >= k and PRFA[LL] < PRFA[-1] and PRFB[LL] < PRFB[-1]:
                    KEY = (parity(PRFA[LL]), parity(PRFB[LL]))
                    current_min = MAPMIN.get(KEY, 999999999)
                    MAPMIN[KEY] = MINIMUM(current_min, PRFA[LL] - PRFB[LL])
                    LL += VONE
                CURKEY = (parity(VONE - parity(PRFA[-1])), parity(PRFB[-1]))
                DIFF = PRFA[-1] - PRFB[-1] - MAPMIN.get(CURKEY, 999999999)
                ANS = MAXIMUM(ANS, DIFF)
                process(RDX + VONE)

            process(VZERO)

        return ANS