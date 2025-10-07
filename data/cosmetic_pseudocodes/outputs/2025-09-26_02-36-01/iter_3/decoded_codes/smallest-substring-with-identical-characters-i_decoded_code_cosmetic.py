class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def longest_uniform_substring(s_arr):
            peak = 0
            streak = 1
            idx = 2
            n = len(s_arr)
            while idx <= n:
                if idx <= n and s_arr[idx - 1] == s_arr[idx - 2]:
                    streak += 1
                else:
                    if peak < streak:
                        peak = streak
                    streak = 1
                idx += 1
            return peak if peak > streak else streak

        result = len(s)
        max_mask = 1 << len(s)
        mask = 0
        while mask < max_mask:
            bitcount = 0
            checker = mask
            while checker > 0:
                bitcount += checker & 1
                checker >>= 1
            if bitcount > numOps:
                mask += 1
                continue

            mutable_s = list(s)
            pos = 0
            while pos < len(s):
                bit_check = mask & (1 << pos)
                if bit_check != 0:
                    mutable_s[pos] = '1' if mutable_s[pos] == '0' else '0'
                pos += 1

            candidate = longest_uniform_substring(mutable_s)
            if result > candidate:
                result = candidate
            mask += 1

        return result