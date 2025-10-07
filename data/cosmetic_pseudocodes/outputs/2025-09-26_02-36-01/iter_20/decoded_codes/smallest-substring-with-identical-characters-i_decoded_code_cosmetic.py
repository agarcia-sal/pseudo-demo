class Solution:
    def minLength(self, s, numOps):
        def longest_uniform_substring(s):
            def equal_chars(a, b):
                return a == b

            max_consecutive = 0
            streak_count = 1
            idx = 1
            while idx < len(s):
                if equal_chars(s[idx], s[idx - 1]):
                    streak_count += 1
                else:
                    if max_consecutive < streak_count:
                        max_consecutive = streak_count
                    streak_count = 1
                idx += 1
            return max(max_consecutive, streak_count)

        def bitcount(x):
            count_accumulator = 0
            temp_value = x
            while temp_value > 0:
                count_accumulator += temp_value & 1
                temp_value >>= 1
            return count_accumulator

        minimal_length = len(s)
        upper_limit = 1 << len(s)

        counter = 0
        while counter < upper_limit:
            if bitcount(counter) > numOps:
                counter += 1
                continue

            array_s = list(s)  # copy string to list for mutability

            for flip_pos in range(len(s)):
                mask = 1 << flip_pos
                if (counter & mask) != 0:
                    array_s[flip_pos] = '1' if array_s[flip_pos] == '0' else '0'

            candidate = longest_uniform_substring(array_s)
            if minimal_length > candidate:
                minimal_length = candidate

            counter += 1

        return minimal_length