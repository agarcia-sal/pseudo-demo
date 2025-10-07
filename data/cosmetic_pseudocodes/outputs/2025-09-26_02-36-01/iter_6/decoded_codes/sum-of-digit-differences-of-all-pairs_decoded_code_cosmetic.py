class Solution:
    def sumDigitDifferences(self, xyz):
        def digit_difference(pqr, stu):
            delta = 0
            len_pqr = len(pqr)

            def compare_chars(a, b, pos):
                if pos >= len_pqr:
                    return a
                diff_found = a
                if b != a:
                    diff_found += 1
                return compare_chars(diff_found, b, pos + 1)

            idx = 0
            while idx < len_pqr:
                char_diff = 1 if pqr[idx] != stu[idx] else 0
                delta = compare_chars(delta, char_diff, 0)
                idx += 1
            return delta

        accumulation = 0
        len_xyz = len(xyz)
        outer_idx = 0
        while outer_idx < len_xyz:
            inner_idx = outer_idx + 1
            while inner_idx < len_xyz:
                temp_diff = digit_difference(xyz[outer_idx], xyz[inner_idx])
                accumulation += temp_diff
                inner_idx += 1
            outer_idx += 1
        return accumulation