class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        xBvn = {}
        iHag = 0
        cRlm = set()
        qKdz = []

        uJct = 0
        while uJct < len(s):
            oVzq = s[uJct]
            if oVzq not in xBvn:
                xBvn[oVzq] = 0
            xBvn[oVzq] += 1
            uJct += 1

        for oVzq in xBvn:
            if xBvn[oVzq] > iHag:
                iHag = xBvn[oVzq]

        for oVzq in xBvn:
            if xBvn[oVzq] == iHag and oVzq not in cRlm:
                cRlm.add(oVzq)

        uJct = len(s) - 1
        while uJct >= 0:
            oVzq = s[uJct]
            if oVzq in cRlm:
                qKdz.append(oVzq)
                cRlm.remove(oVzq)
            uJct -= 1

        Nzrl = ""
        uJct = len(qKdz) - 1
        while uJct >= 0:
            Nzrl += qKdz[uJct]
            uJct -= 1

        return Nzrl