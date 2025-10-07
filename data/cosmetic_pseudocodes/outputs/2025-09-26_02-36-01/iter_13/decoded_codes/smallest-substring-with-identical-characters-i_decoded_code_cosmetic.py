class Solution:
    def minLength(self, s, numOps):
        def count_ones(x):
            total = 0
            n = x
            while n != 0:
                total += n & 1
                n >>= 1
            return total

        def longest_uniform_substring(s):
            def helper(idx, prev_char, current_len, max_len):
                if idx >= len(s):
                    return max(max_len, current_len)
                if s[idx] == prev_char:
                    return helper(idx + 1, prev_char, current_len + 1, max_len)
                else:
                    updated_max = max(max_len, current_len)
                    return helper(idx + 1, s[idx], 1, updated_max)

            if len(s) == 0:
                return 0
            initial_char = s[0]
            return helper(1, initial_char, 1, 0)

        def flip_char(c):
            return '1' if c == '0' else '0'

        def to_char_list(string):
            return [char for char in string]

        min_length = len(s)
        limit = 2 << (len(s) - 1)  # 2^(len(s))
        counter = 0

        while True:
            if counter >= limit:
                break
            if count_ones(counter) > numOps:
                counter += 1
                continue
            new_s = to_char_list(s)
            bit_pos = 0
            while bit_pos < len(s):
                if (counter & (1 << bit_pos)) != 0:
                    new_s[bit_pos] = flip_char(new_s[bit_pos])
                bit_pos += 1
            candidate_length = longest_uniform_substring(new_s)
            if min_length > candidate_length:
                min_length = candidate_length
            counter += 1

        return min_length