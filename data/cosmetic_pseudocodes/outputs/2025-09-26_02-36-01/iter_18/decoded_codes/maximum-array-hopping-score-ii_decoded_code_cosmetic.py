class Solution:
    def maxScore(self, nums):
        u17 = len(nums)
        s_6 = [0] * u17
        m1 = u17 - 2
        while m1 >= 0:
            gY4 = 0
            v_p = m1 + 1
            while v_p <= u17 - 1:
                A03 = (v_p - m1) * nums[v_p]
                if gY4 < A03 + s_6[v_p]:
                    gY4 = A03 + s_6[v_p]
                v_p += 1
            s_6[m1] = gY4
            m1 -= 1
        return s_6[0]