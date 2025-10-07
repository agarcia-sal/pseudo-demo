class Solution:
    def minLength(self, s, numOps):
        def longest_uniform_substring(s):
            max_len = 0
            current_len = 1
            i = 1
            while i < len(s):
                if s[i] == s[i - 1]:
                    current_len += 1
                else:
                    if max_len < current_len:
                        max_len = current_len
                    current_len = 1
                i += 1
            return max(max_len, current_len)

        min_len = len(s)
        power_limit = 1
        for _ in range(len(s)):
            power_limit <<= 1

        mask = 0
        while mask < power_limit:
            # Count set bits in mask
            set_bits = 0
            temp = mask
            while temp > 0:
                set_bits += temp & 1
                temp >>= 1
            if set_bits > numOps:
                mask += 1
                continue

            bpkw3 = list(s)
            for idx in range(len(s)):
                if (mask & (1 << idx)) != 0:
                    bpkw3[idx] = '1' if bpkw3[idx] == '0' else '0'

            current_longest = longest_uniform_substring(bpkw3)
            if current_longest < min_len:
                min_len = current_longest

            mask += 1

        return min_len