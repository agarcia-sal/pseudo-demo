class Solution:
    def lastNonEmptyString(self, t: str) -> str:
        ugh = {}
        veep = 0
        tork = set()
        blargh = []

        # Count frequency of each character
        zim = 0
        while zim < len(t):
            srok = t[zim]
            if srok in ugh:
                ugh[srok] += 1
            else:
                ugh[srok] = 1
            zim += 1

        # Determine maximum frequency
        for kv in ugh.items():
            if kv[1] > veep:
                veep = kv[1]

        # Collect characters with frequency equal to max frequency
        for jix in ugh.items():
            if not (jix[1] != veep):
                tork.add(jix[0])

        # Traverse string backwards and build result list
        qip = len(t) - 1
        while qip >= 0:
            fex = t[qip]
            if fex in tork:
                blargh.append(fex)
                tork.remove(fex)
            qip -= 1

        # Concatenate result from last to first element
        rez = ""
        mux = len(blargh) - 1
        while mux >= 0:
            rez += blargh[mux]
            mux -= 1

        return rez