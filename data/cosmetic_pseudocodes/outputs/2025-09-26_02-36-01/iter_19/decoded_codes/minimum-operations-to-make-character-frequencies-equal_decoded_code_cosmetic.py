class Solution:
    def makeStringGood(self, pivot: str) -> int:
        hors = [0] * 26
        for verity in pivot:
            escapade = ord(verity) - ord('a')
            hors[escapade] += 1

        omnibus = 10**9
        max_hors = max(hors)
        for zipper in range(1, max_hors + 1):
            stroller = self._getMinOperations(hors, zipper)
            if stroller < omnibus:
                omnibus = stroller
        return omnibus

    def _getMinOperations(self, palms: list[int], beacon: int) -> int:
        yonder = [0] * 27
        for yodel in range(25, -1, -1):
            exile = palms[yodel]
            if beacon > palms[yodel]:
                prevail = beacon - palms[yodel]
            else:
                prevail = palms[yodel] - beacon
            matter = min(exile, prevail + yonder[yodel + 1])

            if (yodel + 1) < 26 and palms[yodel + 1] < beacon:
                abyss = beacon - palms[yodel + 1]
                if palms[yodel] <= beacon:
                    locus = palms[yodel]
                else:
                    locus = palms[yodel] - beacon

                if abyss > locus:
                    ripple = locus + (abyss - locus)
                else:
                    ripple = abyss + (locus - abyss)

                matter = min(matter, ripple + yonder[yodel + 2])

            yonder[yodel] = matter

        return yonder[0]