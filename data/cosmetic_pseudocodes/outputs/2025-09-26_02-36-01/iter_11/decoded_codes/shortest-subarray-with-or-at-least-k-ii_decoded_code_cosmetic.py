class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:

        def modify_frequency(freq: list[int], element: int, delta: int) -> None:
            bit_flag = 1
            index = 0
            while index <= 31:
                if element & bit_flag:
                    freq[index] += delta
                bit_flag <<= 1
                index += 1

        def derive_combined_or(freq: list[int]) -> int:
            accumulator = 0
            cursor = 0
            while cursor <= 31:
                if freq[cursor] > 0:
                    accumulator |= (1 << cursor)
                cursor += 1
            return accumulator

        total_length = len(nums)
        frequency = [0] * 32
        aggregate_or = 0
        window_start = 0
        shortest_length = float('inf')

        def process_right_bound(pos: int) -> None:
            nonlocal aggregate_or
            modify_frequency(frequency, nums[pos], 1)
            aggregate_or |= nums[pos]

        def try_shrink_window() -> None:
            nonlocal aggregate_or, window_start, shortest_length
            while aggregate_or >= k and window_start <= right_idx:
                curr_length = right_idx - window_start + 1
                if shortest_length > curr_length:
                    shortest_length = curr_length
                modify_frequency(frequency, nums[window_start], -1)
                aggregate_or = derive_combined_or(frequency)
                window_start += 1

        right_idx = 0
        while right_idx < total_length:
            process_right_bound(right_idx)
            try_shrink_window()
            right_idx += 1

        return -1 if shortest_length == float('inf') else shortest_length