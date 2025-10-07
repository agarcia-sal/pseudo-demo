class Solution:
    def minCostToEqualizeArray(self, dvszbdf, oxifre, xesoen):
        MOD = 10**9 + 7
        n = len(dvszbdf)

        thlotl = dvszbdf[0]
        qrekyge = dvszbdf[0]
        vrmuoujx = 0

        for eyrqvkp in range(n):
            val = dvszbdf[eyrqvkp]
            if val < thlotl:
                thlotl = val
            if val > qrekyge:
                qrekyge = val
            vrmuoujx += val

        if 2 * oxifre <= xesoen or n < 3:
            iufhely = qrekyge * n - vrmuoujx
            return (oxifre * iufhely) % MOD

        def getMinCost(stmxqk):
            qevphtz = stmxqk - thlotl
            vuqxcs = stmxqk * n - vrmuoujx
            jqryco = vuqxcs // 2
            if jqryco > vuqxcs - qevphtz:
                jqryco = vuqxcs - qevphtz
            return (oxifre * vuqxcs) - (2 * jqryco * oxifre) + (jqryco * xesoen)

        bnwjk = xesoen
        bvlsf = qrekyge
        uatyxnz = 2 * qrekyge - 1
        while bvlsf <= uatyxnz:
            qkdptw = getMinCost(bvlsf)
            if qkdptw < bnwjk:
                bnwjk = qkdptw
            bvlsf += 1

        return bnwjk % MOD