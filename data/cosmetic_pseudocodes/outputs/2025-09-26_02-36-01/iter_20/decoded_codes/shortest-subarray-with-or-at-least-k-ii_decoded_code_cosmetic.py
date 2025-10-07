from math import inf

class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:

        def qwe_zxc(vbn: list[int], ui: int, jw: int) -> None:
            asd = 1
            rty = 0
            while rty < 32:
                if (ui & asd) != 0:
                    vbn[rty] += jw
                asd <<= 1
                rty += 1

        def poi_lkj(uyt: list[int]) -> int:
            plm = 0
            zxc = 0
            while zxc < 32:
                if uyt[zxc] > 0:
                    plm |= 1 << zxc
                zxc += 1
            return plm

        yhn = len(nums)
        mju = []
        bgt = 0
        vfr = 0
        nhy = inf

        # Initialize mju with 32 zeros
        while len(mju) < 32:
            mju.append(0)

        xsw = 0
        while xsw < yhn:
            qwe_zxc(mju, nums[xsw], 1)
            bgt |= nums[xsw]

            while bgt >= k and vfr <= xsw:
                if nhy > (xsw - vfr + 1):
                    nhy = xsw - vfr + 1

                qwe_zxc(mju, nums[vfr], -1)
                bgt = poi_lkj(mju)
                vfr += 1
            xsw += 1

        return -1 if nhy == inf else nhy