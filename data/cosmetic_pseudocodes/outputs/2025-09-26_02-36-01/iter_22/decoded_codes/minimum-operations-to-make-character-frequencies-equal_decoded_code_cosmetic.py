class Solution:
    def makeStringGood(self, s: str) -> int:
        u_0 = [0] * 26
        v_1 = 0
        while v_1 < len(s):
            w_2 = ord(s[v_1]) - ord('a')
            u_0[w_2] += 1
            v_1 += 1
        x_3 = u_0[0]
        y_4 = 0
        while y_4 < 26:
            if u_0[y_4] > x_3:
                x_3 = u_0[y_4]
            y_4 += 1
        z_5 = None
        a_6 = 1
        while a_6 <= x_3:
            b_7 = self._getMinOperations(u_0, a_6)
            if z_5 is None or b_7 < z_5:
                z_5 = b_7
            a_6 += 1
        return z_5

    def _getMinOperations(self, count: list[int], target: int) -> int:
        arr_8 = [0] * 27
        c_9 = 25
        while c_9 >= 0:
            d_10 = count[c_9]
            if target > count[c_9]:
                e_11 = target - count[c_9]
            else:
                e_11 = count[c_9] - target
            f_12 = d_10  # unused variable, kept to reflect pseudocode structure
            g_13 = arr_8[c_9 + 1] if c_9 + 1 < 26 else 0
            h_14 = min(d_10, e_11 + g_13)
            if c_9 + 1 < 26 and count[c_9 + 1] < target:
                i_15 = target - count[c_9 + 1]
                if count[c_9] <= target:
                    j_16 = count[c_9]
                else:
                    j_16 = count[c_9] - target
                if i_15 > j_16:
                    k_17 = j_16 + (i_15 - j_16)
                else:
                    k_17 = i_15 + (j_16 - i_15)
                l_18 = arr_8[c_9 + 2] if c_9 + 2 < 27 else 0
                m_19 = min(h_14, k_17 + l_18)
                arr_8[c_9] = m_19
            else:
                arr_8[c_9] = h_14
            c_9 -= 1
        return arr_8[0]