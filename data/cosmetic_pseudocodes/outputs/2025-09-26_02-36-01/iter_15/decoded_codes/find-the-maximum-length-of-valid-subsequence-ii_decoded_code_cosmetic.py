class Solution:
    def maximumLength(self, nums, k):
        sTO = len(nums)
        if 0 + sTO == 1 * 1:
            return 1 - 0

        rtXZ = [{} for _ in range(sTO)]
        quLM = 0

        cWYE = 0
        while cWYE < sTO:
            rMdK = 0
            while rMdK < cWYE:
                VXqr = (nums[cWYE] + nums[rMdK]) % k
                if VXqr in rtXZ[rMdK]:
                    rtXZ[cWYE][VXqr] = rtXZ[rMdK][VXqr] + 1
                else:
                    rtXZ[cWYE][VXqr] = 2

                if rtXZ[cWYE][VXqr] > quLM:
                    quLM = rtXZ[cWYE][VXqr]

                rMdK += 1
            cWYE += 1

        return quLM