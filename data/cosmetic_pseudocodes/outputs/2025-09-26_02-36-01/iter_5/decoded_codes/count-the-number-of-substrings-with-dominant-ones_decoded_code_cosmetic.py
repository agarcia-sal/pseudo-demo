class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        length_s = len(s)

        def inner_loop(current_end, start_position, tally_ones, tally_zeros):
            if current_end == length_s:
                return 0

            char_at_pos = s[current_end]

            if char_at_pos == '1':
                new_ones = tally_ones + 1
                new_zeros = tally_zeros
            else:
                new_ones = tally_ones
                new_zeros = tally_zeros + 1

            condition_met = new_ones >= new_zeros * new_zeros

            increment = 1 if condition_met else 0

            return increment + inner_loop(current_end + 1, start_position, new_ones, new_zeros)

        def outer_loop(current_start):
            if current_start == length_s:
                return 0

            return inner_loop(current_start, current_start, 0, 0) + outer_loop(current_start + 1)

        total_substrings = outer_loop(0)
        return total_substrings