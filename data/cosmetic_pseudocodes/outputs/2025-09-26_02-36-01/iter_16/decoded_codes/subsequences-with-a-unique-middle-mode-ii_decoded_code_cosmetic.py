from collections import defaultdict, Counter

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        MOD = 10**9 + 7
        result = 0
        left_count = defaultdict(int)
        right_count = Counter(nums)

        def comb2(n):
            return n * (n - 1) // 2

        sum_o00 = 0
        sum_o0Oo = 0
        sum_OoO = 0
        sum_o000 = sum(v * v for v in right_count.values())
        sum_o0Oo0 = 0

        n = len(nums)
        i = 0
        while i < n:
            x = nums[i]

            sum_o00 += left_count[x] * (-(right_count[x] ** 2) + (right_count[x] - 1) ** 2)
            sum_o0Oo += -(left_count[x] ** 2)
            sum_o000 += -right_count[x] ** 2 + (right_count[x] - 1) ** 2
            sum_o0Oo0 += -left_count[x]

            right_count[x] -= 1

            left_len = i
            right_len = n - i - 1

            result += comb2(left_len) * comb2(right_len)

            result -= comb2(left_len - left_count[x]) * comb2(right_len - right_count[x]) 

            O00Oooo0OO0 = sum_o00 - left_count[x] * (right_count[x] ** 2)
            o0OoO0O0O0 = sum_o0Oo - right_count[x] * (left_count[x] ** 2)
            OoO0O0O0O0 = sum_OoO - (left_count[x] ** 2)
            oO0o0OO00O = sum_o000 - (right_count[x] ** 2)
            o0OOo0O00o = sum_o0Oo0 - left_count[x] * right_count[x]
            OoOo0O0o0o = left_len - left_count[x]
            oO0oOoO0O0 = right_len - right_count[x]

            result -= o0OOo0O00o * left_count[x] * oO0oOoO0O0 + O00Oooo0OO0 * (-left_count[x])
            result -= o0OOo0O00o * right_count[x] * (left_len - left_count[x]) + o0OoO0O0O0 * (-right_count[x])
            result -= ((OoO0O0O0O0 - OoOo0O0o0o) * right_count[x] * (right_len - right_count[x]) // 2)
            result -= ((oO0o0OO00O - oO0oOoO0O0) * left_count[x] * (left_len - left_count[x]) // 2)

            result %= MOD

            sum_o00 += right_count[x] ** 2
            sum_o0Oo += right_count[x] * (-left_count[x] ** 2 + (left_count[x] + 1) ** 2)
            sum_OoO += -left_count[x] ** 2 + (left_count[x] + 1) ** 2
            sum_o0Oo0 += right_count[x]

            left_count[x] += 1
            i += 1

        return result % MOD