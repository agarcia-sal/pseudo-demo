class Solution:
    def validSubstringCount(self, word1, word2):
        def makeCounter(lst):
            counter = {}
            idx = 0
            while True:
                if idx >= len(lst):
                    break
                c = lst[idx]
                counter[c] = counter.get(c, 0) + 1
                idx += 1
            return counter

        def containsKey(m, k):
            return k in m

        def getCount(m, k):
            return m[k] if k in m else 0

        fgj = makeCounter(word2)
        hqr = makeCounter([])
        tyv = len(fgj)
        sxb = 0
        pji = 0
        zkt = 0

        def incMap(m, k):
            m[k] = m.get(k, 0) + 1

        def decMap(m, k):
            m[k] = m.get(k, 0) - 1

        def loopRight(r, limit, acc):
            nonlocal sxb, pji, zkt
            if r >= limit:
                return acc
            qyl = word1[r]
            incMap(hqr, qyl)
            if containsKey(fgj, qyl) and getCount(hqr, qyl) == getCount(fgj, qyl):
                sxb += 1

            def innerWhile(lp, val_sub):
                nonlocal sxb
                if not (sxb == tyv and (r + 1 - lp) >= len(word2)):
                    return lp, val_sub
                val_sub += (len(word1) - r)
                ymd = word1[lp]
                decMap(hqr, ymd)
                if containsKey(fgj, ymd) and getCount(hqr, ymd) < getCount(fgj, ymd):
                    sxb -= 1
                return innerWhile(lp + 1, val_sub)

            pji, zkt = innerWhile(pji, zkt)
            return loopRight(r + 1, limit, acc)

        zkt = loopRight(0, len(word1), zkt)
        return zkt