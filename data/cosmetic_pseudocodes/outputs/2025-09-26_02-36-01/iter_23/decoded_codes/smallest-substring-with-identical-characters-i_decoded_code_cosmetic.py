class Solution:
    def minLength(self, s, numOps):
        def longest_uniform_substring(s):
            n1 = 0
            n2 = 1

            def recur(pos, n1, n2):
                if pos >= len(s):
                    return n1 if n1 > n2 else n2
                else:
                    if s[pos] == s[pos - 1]:
                        return recur(pos + 1, n1, n2 + 1)
                    else:
                        return recur(pos + 1, max(n1, n2), 1)

            return recur(1, n1, n2)

        v0 = len(s)
        v1 = 1 << len(s)
        v2 = 0

        def count_set_bits(x):
            if x == 0:
                return 0
            else:
                return (x & 1) + count_set_bits(x >> 1)

        def process_bits(i, arr, pos):
            if pos >= len(arr):
                return
            if (i & (1 << pos)) != 0:
                arr[pos] = '1' if arr[pos] == '0' else '0'
            process_bits(i, arr, pos + 1)

        def iter_loop(curr):
            if curr >= v1:
                return v0
            if count_set_bits(curr) > numOps:
                return iter_loop(curr + 1)
            temp_arr = list(s)
            process_bits(curr, temp_arr, 0)
            candidate = longest_uniform_substring(temp_arr)
            nonlocal v0
            if v0 > candidate:
                v0 = candidate
            return iter_loop(curr + 1)

        return iter_loop(v2)