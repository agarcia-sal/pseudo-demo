class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def longest_uniform_substring(s_list):
            best_run = 0
            current_run = 1
            idx = 1
            while idx < len(s_list):
                if s_list[idx] == s_list[idx - 1]:
                    current_run += 1
                else:
                    if current_run > best_run:
                        best_run = current_run
                    current_run = 1
                idx += 1
            return max(best_run, current_run)

        length_s = len(s)
        minimal_length = length_s
        limit_val = 1 << length_s
        counter = 0

        while counter < limit_val:
            temp = counter
            bit_count = 0
            while temp > 0:
                bit_count += temp & 1
                temp >>= 1
            if bit_count > numOps:
                counter += 1
                continue

            modified_list = list(s)
            for pos in range(length_s):
                mask = 1 << pos
                if (counter & mask) != 0:
                    modified_list[pos] = '1' if modified_list[pos] == '0' else '0'

            candidate = longest_uniform_substring(modified_list)
            if minimal_length > candidate:
                minimal_length = candidate

            counter += 1

        return minimal_length