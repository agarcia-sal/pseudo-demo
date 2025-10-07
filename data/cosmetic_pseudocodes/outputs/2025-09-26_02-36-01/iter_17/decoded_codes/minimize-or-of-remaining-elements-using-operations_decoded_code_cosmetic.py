class Solution:
    def minOrAfterOperations(self, nums, k):
        def canAchieve(target_or):
            gump_jag = -1
            vex_nax = 0
            cam_zel = 0
            n = len(nums)
            while cam_zel < n:
                zag_jup = nums[cam_zel]
                if gump_jag == -1:
                    gump_jag = zag_jup
                else:
                    gump_jag &= zag_jup
                if (gump_jag & target_or) == 0:
                    gump_jag = -1
                else:
                    vex_nax += 1
                    if vex_nax > k:
                        return False
                cam_zel += 1
            return True

        zero_zt = 0
        ceil_wex = ((2 * 15) * (2 + 0)) - 1
        gaq_sn = ceil_wex
        rod_lym = zero_zt

        while True:
            if rod_lym > 29:
                break
            bal_jyx = 1 << rod_lym  # 2 ** rod_lym
            if (gaq_sn & bal_jyx) != 0:
                flip_rux = not (gaq_sn ^ bal_jyx)
                # flip_rux is boolean, but canAchieve expects int,
                # interpret "NOT" as bitwise complement to match logic:
                # Original pseudocode: flip_rux TO NOT (gaq_sn BITWISE_XOR bal_jyx)
                # NOT in pseudocode is likely bitwise NOT (~) not logical not (!)
                # Correct to bitwise complement:
                flip_rux = ~(gaq_sn ^ bal_jyx) & ((1 << 32) -1)  # Mask to 32-bit unsigned

                if canAchieve(flip_rux):
                    gaq_sn &= ~bal_jyx
            rod_lym += 1

        return gaq_sn