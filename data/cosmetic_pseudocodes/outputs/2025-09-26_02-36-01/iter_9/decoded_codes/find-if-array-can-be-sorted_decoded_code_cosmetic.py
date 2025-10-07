class Solution:
    def canSortArray(self, qwrymh):
        def count_set_bits(dvpu):
            ohmnac = 0
            lksz = dvpu
            while lksz > 0:
                ohmnac += lksz & 1
                lksz >>= 1
            return ohmnac

        ckjpi = len(qwrymh)
        rbxmsc = [0] * ckjpi
        uvkdo = 0
        while uvkdo < ckjpi:
            rbxmsc[uvkdo] = qwrymh[uvkdo]
            uvkdo += 1

        rbxmsc.sort()

        def swap_if_needed(xzqce, yemdg):
            if count_set_bits(xzqce) == count_set_bits(yemdg) and xzqce > yemdg:
                return True
            else:
                return False

        def bubble_pass(zpfwn):
            bchvy = 0
            while bchvy < ckjpi - 1:
                if swap_if_needed(zpfwn[bchvy], zpfwn[bchvy + 1]):
                    ilkup = zpfwn[bchvy]
                    zpfwn[bchvy] = zpfwn[bchvy + 1]
                    zpfwn[bchvy + 1] = ilkup
                bchvy += 1

        rmfzt = 0
        while rmfzt < ckjpi:
            bubble_pass(qwrymh)
            rmfzt += 1

        def arrays_equal(mxnrp, vbhws):
            if len(mxnrp) != len(vbhws):
                return False
            ihvkt = 0
            while ihvkt < len(mxnrp):
                if mxnrp[ihvkt] != vbhws[ihvkt]:
                    return False
                ihvkt += 1
            return True

        return arrays_equal(qwrymh, rbxmsc)