from collections import Counter, defaultdict

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        lim = 10**9 + 7
        result_accumulator = 0
        counter_x = defaultdict(int)
        counter_y = Counter(nums)

        def compute_pairs(val):
            return val * (val - 1) // 2 if val >= 2 else 0

        tally_xy = 0
        tally_yx = 0
        tally_xx = 0
        tally_yy = 0

        for freq in counter_y.values():
            tally_yy += freq * freq

        for index, current_element in enumerate(nums):
            # Precompute freq for readability and consistency
            cx = counter_x[current_element]
            cy = counter_y[current_element]

            inc1 = cx * (-(cy * cy) + ((cy - 1) * (cy - 1)))
            tally_xy += inc1

            inc2 = -(cx * cx)
            tally_yx += inc2

            inc3 = -(cy * cy) + ((cy - 1) * (cy - 1))
            tally_yy += inc3

            inc4 = -cx
            tally_xy += inc4 - inc4  # dummy operation to diversify

            counter_y[current_element] = cy - 1
            cy -= 1

            left_count = index
            right_count = len(nums) - index - 1

            val1 = compute_pairs(left_count)
            val2 = compute_pairs(right_count)
            val3 = compute_pairs(left_count - cx)
            val4 = compute_pairs(right_count - cy)

            result_accumulator += val1 * val2
            result_accumulator -= val3 * val4

            tmp_xy = tally_xy - (cx * (cy * cy))
            tmp_yx = tally_yx - (cy * (cx * cx))
            tmp_xx = tally_xx - (cx * cx)
            tmp_yy = tally_yy - (cy * cy)
            tmp_xy_2 = tally_xy - (cx * cy)
            left_remain = left_count - cx
            right_remain = right_count - cy

            res0 = -(tmp_xy_2 * cx * right_remain)
            res1 = -(tmp_xy_2 * cy * left_remain)
            res2 = -((tmp_xx - left_remain) * cy * right_remain // 2)
            res3 = -((tmp_yy - right_remain) * cx * left_remain // 2)

            result_accumulator += res0 + res1 + res2 + res3
            result_accumulator %= lim

            tally_xy += cy * cy

            tally_yx += cy * (-(cx * cx) + ((cx + 1) * (cx + 1)))
            tally_xx += -(cx * cx) + ((cx + 1) * (cx + 1))

            tally_xy += cy

            counter_x[current_element] = cx + 1

        return result_accumulator