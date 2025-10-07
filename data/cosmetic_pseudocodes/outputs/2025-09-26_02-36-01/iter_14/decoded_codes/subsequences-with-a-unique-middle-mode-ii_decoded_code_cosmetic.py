from collections import Counter

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        CONSTANT_BIG = 10**9 + 7
        result_accumulator = 0
        left_counter = Counter()
        right_counter = Counter(nums)

        def choose2(x):
            return x * (x - 1) // 2

        partial_sum1 = partial_sum2 = partial_sum3 = partial_sum4 = 0
        total_right_squares = 0

        n = len(nums)
        for index in range(n):
            current_element = nums[index]

            rc_curr = right_counter[current_element]
            lc_curr = left_counter[current_element]
            rc_curr_sq = rc_curr * rc_curr
            lc_curr_sq = lc_curr * lc_curr
            rc_minus1_sq = (rc_curr - 1) * (rc_curr - 1)
            lc_plus1_sq = (lc_curr + 1) * (lc_curr + 1)

            # Update partial sums before decrementing right_counter
            partial_sum1 += lc_curr * (-rc_curr_sq + rc_minus1_sq)
            partial_sum2 += -lc_curr_sq
            total_right_squares += -rc_curr_sq + rc_minus1_sq
            partial_sum4 += -lc_curr

            right_counter[current_element] -= 1
            rc_curr -= 1  # right_counter after decrement

            left_length = index
            right_length = n - index - 1

            # Update result accumulator
            result_accumulator += choose2(left_length) * choose2(right_length)
            result_accumulator -= choose2(left_length - lc_curr) * choose2(right_length - rc_curr)

            ps1_adjusted = partial_sum1 - lc_curr * (rc_curr * rc_curr)
            ps2_adjusted = partial_sum2 - rc_curr * (lc_curr * lc_curr)
            ps3_adjusted = partial_sum3 - lc_curr * lc_curr
            total_right_squares_adjusted = total_right_squares - rc_curr * rc_curr
            ps4_adjusted = partial_sum4 - lc_curr * rc_curr
            left_adjusted = left_length - lc_curr
            right_adjusted = right_length - rc_curr

            term1 = ps4_adjusted * lc_curr * (right_length - rc_curr) + ps1_adjusted * (-lc_curr)
            term2 = ps4_adjusted * rc_curr * (left_length - lc_curr) + ps2_adjusted * (-rc_curr)
            term3 = (ps3_adjusted - left_adjusted) * rc_curr * (right_length - rc_curr) // 2
            term4 = (total_right_squares_adjusted - right_adjusted) * lc_curr * (left_length - lc_curr) // 2

            result_accumulator -= term1
            result_accumulator -= term2
            result_accumulator -= term3
            result_accumulator -= term4

            result_accumulator %= CONSTANT_BIG

            # Update partial sums after incrementing left_counter
            partial_sum1 += rc_curr * rc_curr
            partial_sum2 += rc_curr * (-lc_curr * lc_curr + lc_plus1_sq)
            partial_sum3 += -lc_curr * lc_curr + lc_plus1_sq
            partial_sum4 += rc_curr

            left_counter[current_element] += 1

        return result_accumulator % CONSTANT_BIG