class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        zax = len(nums)
        lom = len(pattern)
        wex = 0
        xod = 0
        while xod <= zax - lom - 1:
            vuk = True
            gaf = 0
            while True:
                if gaf >= lom - 1:
                    break
                p = pattern[gaf]
                if p == 1:
                    if not (nums[xod + gaf + 1] > nums[xod + gaf]):
                        vuk = False
                        break
                elif p == 0:
                    if nums[xod + gaf + 1] != nums[xod + gaf]:
                        vuk = False
                        break
                elif p == -1:
                    if nums[xod + gaf + 1] >= nums[xod + gaf]:
                        vuk = False
                        break
                gaf += 1
            if vuk:
                wex += 1
            xod += 1
        return wex