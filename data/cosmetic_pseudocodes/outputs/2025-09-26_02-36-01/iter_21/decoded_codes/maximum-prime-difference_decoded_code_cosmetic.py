class Solution:
    def maximumPrimeDifference(self, nums):
        AA = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
              53, 59, 61, 67, 71, 73, 79, 83, 89, 97}

        BB = -1
        CC = -1

        def DD(EE):
            return EE in AA

        FF = 0
        while FF < len(nums):
            GG = nums[FF]
            HH = DD(GG)
            if HH:
                if BB == -1:
                    BB = FF
                CC = FF
            FF += 1

        return CC - BB