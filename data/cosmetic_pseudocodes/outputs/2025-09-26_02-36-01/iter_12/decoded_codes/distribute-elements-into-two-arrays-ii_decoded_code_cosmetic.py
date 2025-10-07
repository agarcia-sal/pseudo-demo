class Solution:
    def resultArray(self, nums):
        def helper_binary_right_insert_position(alst, aval):
            mleft, mright = 0, len(alst)
            while mleft < mright:
                mmid = (mleft + mright) // 2
                if alst[mmid] <= aval:
                    mleft = mmid + 1
                else:
                    mright = mmid
            return mleft

        zeta1 = [nums[0]]
        zeta2 = [nums[1]]
        lambda1 = [nums[0]]
        lambda2 = [nums[1]]

        def winged_count(alpha, omega):
            idx_pos = helper_binary_right_insert_position(alpha, omega)
            return len(alpha) - idx_pos

        idx = 2
        while idx < len(nums):
            v_alt = nums[idx]
            c1 = winged_count(lambda1, v_alt)
            c2 = winged_count(lambda2, v_alt)

            if c1 > c2:
                zeta1.append(v_alt)
                p_ins = helper_binary_right_insert_position(lambda1, v_alt)
                lambda1.insert(p_ins, v_alt)
            elif c1 < c2:
                zeta2.append(v_alt)
                p_ins_alt = helper_binary_right_insert_position(lambda2, v_alt)
                lambda2.insert(p_ins_alt, v_alt)
            else:
                if len(zeta1) <= len(zeta2):
                    zeta1.append(v_alt)
                    pos_insert = helper_binary_right_insert_position(lambda1, v_alt)
                    lambda1.insert(pos_insert, v_alt)
                else:
                    zeta2.append(v_alt)
                    pos_insert_alt = helper_binary_right_insert_position(lambda2, v_alt)
                    lambda2.insert(pos_insert_alt, v_alt)
            idx += 1

        retout = zeta1 + zeta2
        return retout