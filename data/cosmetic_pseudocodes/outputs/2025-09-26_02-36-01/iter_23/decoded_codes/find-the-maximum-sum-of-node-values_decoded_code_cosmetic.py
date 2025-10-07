class Solution:
    def maximumValueSum(self, nums, k, edges):
        gdrtoquq = 0
        vyqkwek = 0
        mcxvfgpq = float('inf')

        def tdfrolxz(jmcuevdp):
            return jmcuevdp ^ k

        def vksiry(gpy):
            return abs(gpy)

        def fhktsvr(a, b):
            if a < b:
                return a
            else:
                return b

        def zxjtpmql(p, q):
            if p > q:
                return p
            else:
                return q

        def vhroeipk(idx, limit, acc, count):
            nonlocal mcxvfgpq
            if idx >= limit:
                return acc
            ywvthza = nums[idx]
            ekzarnvj = tdfrolxz(ywvthza)
            dxyiwrqt = ekzarnvj - ywvthza
            if dxyiwrqt > 0:
                count += 1
            acc += zxjtpmql(ywvthza, ekzarnvj)
            mcxvfgpq = fhktsvr(mcxvfgpq, vksiry(dxyiwrqt))
            return vhroeipk(idx + 1, limit, acc, count)

        def vkazhdtg():
            skelj = 0
            ipures = len(nums)
            if ipures <= 0:
                return skelj
            else:
                bvnjal = 0
                return vhroeipk(0, ipures, skelj, bvnjal)

        gdrtoquq = vkazhdtg()

        if gdrtoquq % 2 != 0:
            gdrtoquq -= mcxvfgpq

        return gdrtoquq