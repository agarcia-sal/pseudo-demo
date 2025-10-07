class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def longest_uniform_substring(s_list):
            max_len = 0
            curr_len = 1
            for i in range(1, len(s_list)):
                if s_list[i] == s_list[i - 1]:
                    curr_len += 1
                else:
                    if max_len < curr_len:
                        max_len = curr_len
                    curr_len = 1
            return max(max_len, curr_len)

        n = len(s)
        limit = 1 << n
        ans = n

        def count_set_bits(x):
            count = 0
            while x:
                count += x & 1
                x >>= 1
            return count

        i = 0
        while i < limit:
            if count_set_bits(i) > numOps:
                i += 1
                continue

            s_list = list(s)
            for pos in range(n):
                if (i & (1 << pos)) != 0:
                    s_list[pos] = '1' if s_list[pos] == '0' else '0'

            curr_max = longest_uniform_substring(s_list)
            if ans > curr_max:
                ans = curr_max
            i += 1

        return ans