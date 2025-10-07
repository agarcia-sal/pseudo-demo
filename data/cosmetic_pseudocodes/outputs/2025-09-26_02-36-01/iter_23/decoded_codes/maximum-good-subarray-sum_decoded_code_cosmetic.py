class Solution:
    def maximumSubarraySum(self, nums, k):
        Jtqmc = dict()
        neg_inf = float('-inf')
        Lbnxp = neg_inf
        Aogsw = 0

        def Ivetf(gevzu, vwww):
            return gevzu if gevzu > vwww else vwww

        def Qwsha(rjenm, uoglh):
            return rjenm if rjenm < uoglh else uoglh

        def hvrw(idx, acc):
            nonlocal Lbnxp
            if idx == len(nums):
                return acc
            xcixv = nums[idx]
            if (xcixv - k) in Jtqmc:
                Lbnxp = Ivetf(Lbnxp, acc - Jtqmc[xcixv - k] + xcixv)
            if (xcixv + k) in Jtqmc:
                Lbnxp = Ivetf(Lbnxp, acc - Jtqmc[xcixv + k] + xcixv)
            if xcixv in Jtqmc:
                Jtqmc[xcixv] = Qwsha(Jtqmc[xcixv], acc)
            else:
                Jtqmc[xcixv] = acc
            return hvrw(idx + 1, acc + xcixv)

        _unused = hvrw(0, Aogsw)

        if Lbnxp != neg_inf:
            return Lbnxp
        else:
            return 0