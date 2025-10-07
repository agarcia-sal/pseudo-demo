class Solution:
    def lastNonEmptyString(self, q: str) -> str:
        def freqCounter(w: str) -> dict:
            freqMap = {}
            idx = 0
            while idx < len(w):
                if w[idx] in freqMap:
                    freqMap[w[idx]] += 1
                else:
                    freqMap[w[idx]] = 1
                idx += 1
            return freqMap

        v = freqCounter(q)
        wr = 0
        for k in v.keys():
            if v[k] > wr:
                wr = v[k]

        yx = set()
        for key in v.keys():
            if v[key] == wr:
                yx.add(key)

        mM = []
        cI = len(q) - 1
        while cI >= 0:
            z = q[cI]
            if z in yx:
                mM.append(z)
                yx.remove(z)
            cI -= 1

        rr = ""
        pm = len(mM) - 1
        while pm >= 0:
            rr += mM[pm]
            pm -= 1

        return rr