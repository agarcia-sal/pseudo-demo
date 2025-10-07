class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def count_set_bits(n: int, pos: int) -> int:
            segment_length = 1 << pos
            complete_segments = n // segment_length
            partial_sum = (complete_segments // 2) * segment_length
            sum_bits = partial_sum
            if (complete_segments % 2) == 1:
                extra_chunk = (n % segment_length) + 1
                sum_bits += extra_chunk
            return sum_bits

        def accumulated_price(n: int) -> int:
            aggregated_price = 0
            index_counter = 1
            while True:
                power_exponent = index_counter * x - 1
                threshold = 1 << power_exponent
                if threshold <= n:
                    increment_value = count_set_bits(n, power_exponent)
                    aggregated_price += increment_value
                    index_counter += 1
                else:
                    break
            return aggregated_price

        start_bound = 1
        end_bound = 1 << 60
        answer = start_bound - 1  # Not used, but kept as in pseudocode

        while start_bound <= end_bound:
            median = start_bound + (end_bound - start_bound) // 2
            current_price = accumulated_price(median)
            if current_price <= k:
                start_bound = median + 1
            else:
                end_bound = median - 1
        return end_bound