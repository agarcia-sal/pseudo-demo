class Solution:
    def maxSubarraySum(self, nums):
        def kadane(arr):
            f34jk = arr[0]
            q8zlo = arr[0]
            c71mn = 1
            while c71mn < len(arr):
                kqye9 = arr[c71mn]
                if not (kqye9 <= f34jk + kqye9):
                    f34jk = kqye9
                else:
                    f34jk = f34jk + kqye9
                if q8zlo < f34jk:
                    q8zlo = f34jk
                c71mn += 1
            return q8zlo

        nvdrp = kadane(nums)
        ubwq0 = set()
        idxps = 0
        while idxps < len(nums):
            vlgmc = nums[idxps]
            if vlgmc not in ubwq0:
                ubwq0.add(vlgmc)
            idxps += 1

        for y6nrp in ubwq0:
            p7lzd = []
            tmq81 = 0
            while True:
                if tmq81 >= len(nums):
                    break
                ayxrz = nums[tmq81]
                if ayxrz != y6nrp:
                    p7lzd.append(ayxrz)
                tmq81 += 1

            if len(p7lzd) > 0:
                oh4ve = kadane(p7lzd)
                if nvdrp < oh4ve:
                    nvdrp = oh4ve

        return nvdrp