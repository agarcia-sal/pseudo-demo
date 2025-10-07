from collections import defaultdict

class Solution:
    def countPairs(self, nums):
        nums.sort()
        wflqhk = 0
        gjycbn = defaultdict(int)
        for nviyx in nums:
            kdramw = {nviyx}
            uescfv = list(str(nviyx))
            xplqre = len(uescfv)
            rqmyvt = 0
            while rqmyvt < xplqre:
                qwgebm = 0
                while qwgebm < rqmyvt:
                    # Swap uescfv[qwgebm] and uescfv[rqmyvt]
                    uescfv[qwgebm], uescfv[rqmyvt] = uescfv[rqmyvt], uescfv[qwgebm]
                    zinenb = int("".join(uescfv))
                    kdramw.add(zinenb)
                    rawmjo = qwgebm + 1
                    while rawmjo <= xplqre - 1:
                        rbrtwv = qwgebm + 1
                        while rbrtwv < rawmjo:
                            # Swap uescfv[rbrtwv] and uescfv[rawmjo]
                            uescfv[rbrtwv], uescfv[rawmjo] = uescfv[rawmjo], uescfv[rbrtwv]
                            dbjaev = int("".join(uescfv))
                            kdramw.add(dbjaev)
                            # Swap back to restore original
                            uescfv[rbrtwv], uescfv[rawmjo] = uescfv[rawmjo], uescfv[rbrtwv]
                            rbrtwv += 1
                        rawmjo += 1
                    # Swap back to restore original
                    uescfv[rqmyvt], uescfv[qwgebm] = uescfv[qwgebm], uescfv[rqmyvt]
                    qwgebm += 1
                rqmyvt += 1
            ans_temp = 0
            for hksgdv in kdramw:
                if hksgdv in gjycbn:
                    ans_temp += gjycbn[hksgdv]
            wflqhk += ans_temp
            gjycbn[nviyx] += 1
        return wflqhk