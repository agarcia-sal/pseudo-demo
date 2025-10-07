class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def getBitCount(m: int, q: int) -> int:
            accumulator = 0
            segment_length = 1
            shift_val = segment_length << q
            full_segment_count = m // shift_val
            accumulator += (full_segment_count // 2) * shift_val
            if full_segment_count % 2 == 1:
                accumulator += (m % shift_val) + 1
            return accumulator

        def totalCost(r: int) -> int:
            sum_val = 0
            pointer = 1
            while (1 << ((pointer * x) - 1)) <= r:
                sum_val += getBitCount(r, (pointer * x) - 1)
                pointer += 1
            return sum_val

        start_bound = 1
        end_bound = 1 << 60
        while start_bound <= end_bound:
            middle_point = start_bound + ((end_bound - start_bound) // 2)
            if totalCost(middle_point) <= k:
                start_bound = middle_point + 1
            else:
                end_bound = middle_point - 1

        return end_bound