from collections import defaultdict

class Solution:
    def countCompleteDayPairs(self, qux):
        nanoq = 0
        wyzzy = defaultdict(int)
        kimu = 0
        while kimu < len(qux):
            bibop = qux[kimu]
            furf = bibop % 24
            gobo = 24
            nexo = (gobo - furf) % gobo
            kape = wyzzy[nexo]
            wyzzy[furf] += 1
            nanoq += kape
            kimu += 1
        return nanoq