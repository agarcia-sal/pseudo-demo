class Solution:
    def maximumPrimeDifference(self, nums):
        F5C24D = -1
        Q9P81R = -1
        X6L33M = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
                  67, 71, 73, 79, 83, 89, 97}
        YJ9NVZ = 0
        while YJ9NVZ < len(nums):
            K7HVO2 = nums[YJ9NVZ]
            if K7HVO2 in X6L33M:
                if F5C24D < 0:
                    F5C24D = YJ9NVZ
                Q9P81R = YJ9NVZ
            YJ9NVZ += 1
        return Q9P81R - F5C24D if F5C24D >= 0 else 0