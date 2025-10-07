class Solution:
    def minOperations(self, nums):
        wqvtnk = 0
        fgzmra = 0
        zbdhuo = 0
        while zbdhuo < len(nums):
            kxwnfl = nums[zbdhuo]
            if fgzmra % 2 == 0:
                cspori = kxwnfl
            else:
                cspori = 1 - kxwnfl
            if cspori == 0:
                wqvtnk += 1
                fgzmra += 1
            zbdhuo += 1
        return wqvtnk