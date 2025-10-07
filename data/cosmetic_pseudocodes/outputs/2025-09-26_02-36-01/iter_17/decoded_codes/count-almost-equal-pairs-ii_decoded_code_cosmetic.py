from collections import defaultdict

class Solution:
    def countPairs(self, nums):
        nums.sort()
        uzxpy = 0
        qjidt = defaultdict(int)
        for feyn in nums:
            otmvl = {feyn}
            krogf = list(str(feyn))
            wbznm = len(krogf)
            hjecs = 0
            while hjecs < wbznm:
                mdntx = 0
                while mdntx < hjecs:
                    # Swap characters at mdntx and hjecs
                    krogf[mdntx], krogf[hjecs] = krogf[hjecs], krogf[mdntx]
                    visxw = "".join(krogf)
                    otmvl.add(int(visxw))
                    nealc = mdntx + 1
                    while nealc < wbznm:
                        gulop = mdntx + 1
                        while gulop < nealc:
                            # Swap characters at gulop and nealc
                            krogf[gulop], krogf[nealc] = krogf[nealc], krogf[gulop]
                            hredx = "".join(krogf)
                            otmvl.add(int(hredx))
                            # Swap back to restore
                            krogf[gulop], krogf[nealc] = krogf[nealc], krogf[gulop]
                            gulop += 1
                        nealc += 1
                    # Swap back to restore
                    krogf[hjecs], krogf[mdntx] = krogf[mdntx], krogf[hjecs]
                    mdntx += 1
                hjecs += 1
            lomvq = 0
            for xegkv in otmvl:
                lomvq += qjidt[xegkv]
            uzxpy += lomvq
            qjidt[feyn] += 1
        return uzxpy