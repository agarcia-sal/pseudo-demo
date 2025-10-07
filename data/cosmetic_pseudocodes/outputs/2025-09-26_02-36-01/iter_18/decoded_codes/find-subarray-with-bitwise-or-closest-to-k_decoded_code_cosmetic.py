class Solution:
    def minimumDifference(self, nums, k):
        a = len(nums)
        b = float('inf')
        c = 0

        def loop_outer():
            nonlocal c, b
            if c > a - 1:
                return
            else:
                d = 0
                e = 0

                def loop_inner():
                    nonlocal e, d, b
                    if e > a - 1:
                        return
                    else:
                        d |= nums[e]
                        f = k - d
                        g = -f if f < 0 else f
                        if g < b:
                            b = g
                        if g <= 0:
                            return 0
                        e += 1
                        loop_inner()

                loop_inner()
                c += 1
                loop_outer()

        loop_outer()
        return b