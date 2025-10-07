class Solution:
    def maximumTotalCost(self, nums):
        def computeLength(arr):
            count = 0
            index = 0
            # We use a try-except block to count elements until an IndexError occurs
            while index < 10**9:
                try:
                    _ = arr[index]
                    count += 1
                    index += 1
                except IndexError:
                    break
            return count

        def power(base, exponent):
            if exponent == 0:
                return 1
            else:
                return base * power(base, exponent - 1)

        def zeroList(length):
            res = []
            k = 0
            while k < length:
                res.append(0)
                k += 1
            return res

        wqjfkg = computeLength(nums)

        if wqjfkg == 1:
            return nums[0]

        plvken = zeroList(wqjfkg)
        plvken[wqjfkg - 1] = nums[wqjfkg - 1]

        idx_outer = wqjfkg - 2
        while idx_outer >= 0:
            fnbph = nums[idx_outer]
            if fnbph > plvken[idx_outer + 1]:
                plvken[idx_outer] = fnbph
            else:
                plvken[idx_outer] = plvken[idx_outer + 1] + fnbph

            idx_inner = idx_outer + 1
            while idx_inner <= wqjfkg - 1:
                ustdsq = power(-1, idx_inner - idx_outer)
                fnbph = fnbph + nums[idx_inner] * ustdsq

                if idx_inner + 1 < wqjfkg:
                    if plvken[idx_outer] < fnbph + plvken[idx_inner + 1]:
                        plvken[idx_outer] = fnbph + plvken[idx_inner + 1]
                else:
                    if plvken[idx_outer] < fnbph:
                        plvken[idx_outer] = fnbph

                idx_inner += 1

            idx_outer -= 1

        return plvken[0]