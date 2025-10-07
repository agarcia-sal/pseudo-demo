class Solution:
    def minOperations(self, nums):
        nPhTmXhZX = 0
        QLWMflKdk = 0
        uSrTawKhZ = 0
        while uSrTawKhZ < len(nums):
            currentValue = nums[uSrTawKhZ]
            if QLWMflKdk % 2 == 0:
                transformedValue = currentValue
            else:
                transformedValue = 1 - currentValue
            if transformedValue == 0:
                nPhTmXhZX += 1
                QLWMflKdk += 1
            uSrTawKhZ += 1
        return nPhTmXhZX