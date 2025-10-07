class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def longest_uniform_substring(s_list):
            peak_length = 0
            streak = 1
            idx = 1
            while idx < len(s_list):
                if s_list[idx] == s_list[idx - 1]:
                    streak += 1
                else:
                    if streak > peak_length:
                        peak_length = streak
                    streak = 1
                idx += 1
            return max(peak_length, streak)

        minimal_length = len(s)
        boundary = 1 << len(s)
        counter = 0
        s_list = list(s)
        while counter < boundary:
            # Count bits set in counter
            bitcount = 0
            temp = counter
            while temp > 0:
                bitcount += temp & 1
                temp >>= 1
            if bitcount > numOps:
                counter += 1
                continue
            altered = s_list[:]
            pos = 0
            while pos < len(s):
                if (counter & (1 << pos)) != 0:
                    altered[pos] = '1' if altered[pos] == '0' else '0'
                pos += 1
            current_length = longest_uniform_substring(altered)
            if minimal_length > current_length:
                minimal_length = current_length
            counter += 1

        return minimal_length