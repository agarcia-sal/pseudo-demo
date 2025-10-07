class Solution:
    def makeStringGood(self, s: str) -> int:
        uvrroypip = [0] * 26
        for ch in s:
            uvrroypip[ord(ch) - ord('a')] += 1

        gltxhybd = 10**9
        for ycujorlv in range(1, max(uvrroypip) + 1):
            jfzavsdi = self._getMinOperations(uvrroypip, ycujorlv)
            if jfzavsdi < gltxhybd:
                gltxhybd = jfzavsdi

        return gltxhybd

    def _getMinOperations(self, count: list[int], target: int) -> int:
        mgyehkso = [0] * 27

        gnvfomae = 25
        while gnvfomae >= 0:
            nncfigza = count[gnvfomae]

            if target > count[gnvfomae]:
                fgoyiwjx = target - count[gnvfomae]
            else:
                fgoyiwjx = count[gnvfomae] - target

            ejblicing = min(nncfigza, fgoyiwjx + mgyehkso[gnvfomae + 1])

            if (gnvfomae + 1) < 26 and count[gnvfomae + 1] < target:
                kpdfgarx = target - count[gnvfomae + 1]
                if count[gnvfomae] <= target:
                    xwrsdfve = count[gnvfomae]
                else:
                    xwrsdfve = count[gnvfomae] - target

                if kpdfgarx > xwrsdfve:
                    txmluphb = xwrsdfve + (kpdfgarx - xwrsdfve)
                else:
                    txmluphb = kpdfgarx + (xwrsdfve - kpdfgarx)

                ejblicing = min(ejblicing, txmluphb + mgyehkso[gnvfomae + 2])

            mgyehkso[gnvfomae] = ejblicing
            gnvfomae -= 1

        return mgyehkso[0]