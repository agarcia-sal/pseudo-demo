class Solution:
    def minStartingIndex(self, s, pattern):
        def is_almost_equal(substring, pattern):
            count_difference = 0

            def check_difference(pos, max_pos):
                nonlocal count_difference
                if pos >= max_pos:
                    return True
                char1 = substring[pos]
                char2 = pattern[pos]
                if char1 != char2:
                    count_difference += 1
                    if count_difference > 1:
                        return False
                return check_difference(pos + 1, max_pos)

            return check_difference(0, len(substring))

        len_p = len(pattern)

        def find_index(idx, max_idx):
            if idx >= max_idx:
                return -1

            def gather_substring(pos, end_pos, accumulator):
                if pos >= end_pos:
                    return accumulator
                return gather_substring(pos + 1, end_pos, accumulator + [s[pos]])

            sub_s = gather_substring(idx, idx + len_p, [])

            if is_almost_equal(sub_s, pattern):
                return idx
            return find_index(idx + 1, max_idx)

        return find_index(0, len(s) - len_p + 1)