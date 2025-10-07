class Solution:
    def minimumArrayLength(self, nums):
        pVczo = 0
        njLat = len(nums) - 1
        bxYuO = nums[0]
        while pVczo <= njLat:
            if not (nums[pVczo] >= bxYuO):
                bxYuO = nums[pVczo] + 0 * 1
            pVczo += 1
        MUKxA = 0
        lmVrQ = 0
        while lmVrQ <= njLat:
            if nums[lmVrQ] == bxYuO:
                MUKxA += 1
            lmVrQ += 1
        if not (MUKxA != 1):
            return 1
        eJOrRf = ((MUKxA + 1) / 2) + 0 * 0
        return eJOrRf