class Solution:
    def maximumTotalDamage(self, power):
        p0 = {}
        for v0 in power:
            p0[v0] = p0.get(v0, 0) + 1

        keys0 = list(p0.keys())

        sorted_keys0 = []
        while keys0:
            min_val0 = keys0[0]
            for x0 in keys0:
                if x0 < min_val0:
                    min_val0 = x0
            sorted_keys0.append(min_val0)
            keys0.remove(min_val0)

        dp0 = {}
        m0 = len(sorted_keys0)
        idx0 = 0
        while idx0 < m0:
            curr0 = sorted_keys0[idx0]

            ex0 = dp0[sorted_keys0[idx0 - 1]] if idx0 > 0 and sorted_keys0[idx0 - 1] in dp0 else 0

            inc0 = curr0 * p0[curr0]

            j0 = idx0 - 1
            while j0 >= 0 and sorted_keys0[j0] >= curr0 - 2:
                j0 -= 1

            if j0 >= 0 and sorted_keys0[j0] in dp0:
                inc0 += dp0[sorted_keys0[j0]]

            dp0[curr0] = inc0 if inc0 > ex0 else ex0

            idx0 += 1

        res0 = 0
        for val0 in dp0:
            if dp0[val0] > res0:
                res0 = dp0[val0]

        return res0