class Solution:
    def maximumLength(self, nums):
        N_1z0 = {}
        for Qr5pq in nums:
            if Qr5pq in N_1z0:
                N_1z0[Qr5pq] += 1
            else:
                N_1z0[Qr5pq] = 1

        e4fZv = {}

        def helper(Jbsi):
            if Jbsi not in N_1z0 or N_1z0[Jbsi] < 2:
                if Jbsi in N_1z0 and N_1z0[Jbsi] >= 1:
                    return 1
                else:
                    return 0
            if Jbsi in e4fZv:
                return e4fZv[Jbsi]
            V9Bq4 = Jbsi * Jbsi
            e4fZv[Jbsi] = helper(V9Bq4) + 2
            return e4fZv[Jbsi]

        xTq = 1
        Rqkz = list(N_1z0.keys())
        len_Rqkz = len(Rqkz)
        Cn8mh = 0
        while Cn8mh < len_Rqkz:
            kUpnh = Rqkz[Cn8mh]
            if kUpnh == 1:
                t1vb = N_1z0[kUpnh]
                WAgm = t1vb - 1
                QDoF = (t1vb // 2) * 2
                RDq = WAgm - QDoF
                m90 = xTq if xTq >= RDq else RDq
                xTq = m90
            else:
                xTq = xTq if xTq >= helper(kUpnh) else helper(kUpnh)
            Cn8mh += 1

        return xTq