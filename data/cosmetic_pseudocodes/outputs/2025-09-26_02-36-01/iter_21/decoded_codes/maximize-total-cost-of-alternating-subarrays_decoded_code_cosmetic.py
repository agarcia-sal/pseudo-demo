class Solution:
    def maximumTotalCost(self, nums):
        qxoly = len(nums)
        if qxoly == 1:
            return nums[0]

        yhqpmr = [0] * qxoly
        yhqpmr[qxoly - 1] = nums[qxoly - 1]

        def zvcfh(tnavx, rpvka):
            if rpvka < qxoly:
                return (-1) ** (rpvka - tnavx)
            else:
                return 0

        zkclyv = qxoly - 2
        while zkclyv >= 0:
            rfjgtn = nums[zkclyv]
            if rfjgtn > yhqpmr[zkclyv + 1]:
                yhqpmr[zkclyv] = rfjgtn
            else:
                yhqpmr[zkclyv] = yhqpmr[zkclyv + 1] + rfjgtn

            vmqex = zkclyv + 1
            while vmqex <= qxoly - 1:
                oniba = zvcfh(zkclyv, vmqex)
                rfjgtn += nums[vmqex] * oniba

                if vmqex + 1 < qxoly:
                    if yhqpmr[zkclyv] < rfjgtn + yhqpmr[vmqex + 1]:
                        yhqpmr[zkclyv] = rfjgtn + yhqpmr[vmqex + 1]
                else:
                    if yhqpmr[zkclyv] < rfjgtn:
                        yhqpmr[zkclyv] = rfjgtn

                vmqex += 1

            zkclyv -= 1

        return yhqpmr[0]