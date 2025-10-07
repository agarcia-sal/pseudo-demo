class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def count_set_bits(n: int, bitpos: int) -> int:
            segment_length = 1 << bitpos  # 2^bitpos
            completed_segments = n // segment_length
            partial_segment_full = completed_segments // 2
            tally = partial_segment_full * segment_length
            if completed_segments % 2 == 1:
                remainder = n % segment_length
                tally += remainder + 1
            return tally

        def accumulated_price(limit: int) -> int:
            def accumulate_recursive(index: int, accumulator: int) -> int:
                power = (index * x) - 1
                if power < 0 or (1 << power) > limit:
                    return accumulator
                addition = count_set_bits(limit, power)
                return accumulate_recursive(index + 1, accumulator + addition)
            return accumulate_recursive(1, 0)

        def binary_search(low_val: int, high_val: int) -> int:
            if low_val > high_val:
                return high_val
            middle_val = low_val + (high_val - low_val) // 2
            price_at_mid = accumulated_price(middle_val)
            if price_at_mid <= k:
                return binary_search(middle_val + 1, high_val)
            else:
                return binary_search(low_val, middle_val - 1)

        start_range = 1
        end_range = 1 << 60  # 2^60
        result = binary_search(start_range, end_range)
        return result