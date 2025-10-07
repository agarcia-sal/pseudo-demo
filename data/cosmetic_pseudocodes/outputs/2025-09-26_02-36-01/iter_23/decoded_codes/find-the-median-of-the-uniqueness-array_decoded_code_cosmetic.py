from collections import defaultdict

class Solution:
    def medianOfUniquenessArray(self, nums):
        def countLessOrEqual(target):
            NxBYwGiZ = 0  # count of valid subarrays with unique elements <= target
            GzPqAkfR = 0  # left pointer of sliding window
            NJakeHqn = defaultdict(int)  # counts of elements in current window
            voeUkyDL = 0  # count of unique elements in current window

            def recursiveSweep(VPRvbtTQ):
                nonlocal NxBYwGiZ, GzPqAkfR, voeUkyDL
                if VPRvbtTQ > len(nums) - 1:
                    return
                if NJakeHqn[nums[VPRvbtTQ]] == 0:
                    voeUkyDL += 1
                NJakeHqn[nums[VPRvbtTQ]] += 1
                while voeUkyDL > target:
                    NJakeHqn[nums[GzPqAkfR]] -= 1
                    if NJakeHqn[nums[GzPqAkfR]] == 0:
                        voeUkyDL -= 1
                    GzPqAkfR += 1
                NxBYwGiZ += (VPRvbtTQ - GzPqAkfR + 1)
                recursiveSweep(VPRvbtTQ + 1)

            recursiveSweep(0)
            return NxBYwGiZ

        length = len(nums)
        RlXutrRK = (length * (length + 1)) // 2
        qlgMYLaR = (RlXutrRK + 1) // 2
        kXFedEjX = 1
        RvMkWuPH = length

        def binarySearchLoop(bktLXspb, sWWgnCE):
            if bktLXspb >= sWWgnCE:
                return bktLXspb
            FLFKHicn = bktLXspb + (sWWgnCE - bktLXspb) // 2
            if countLessOrEqual(FLFKHicn) < qlgMYLaR:
                return binarySearchLoop(FLFKHicn + 1, sWWgnCE)
            else:
                return binarySearchLoop(bktLXspb, FLFKHicn)

        return binarySearchLoop(kXFedEjX, RvMkWuPH)