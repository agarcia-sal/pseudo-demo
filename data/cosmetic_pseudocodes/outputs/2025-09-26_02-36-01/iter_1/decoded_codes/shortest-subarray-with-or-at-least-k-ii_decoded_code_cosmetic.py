class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        def adjust_count(bit_counts: list[int], number: int, delta: int) -> None:
            bit_flag = 1
            for position in range(32):
                if (number & bit_flag) != 0:
                    bit_counts[position] += delta
                bit_flag <<= 1

        def calculate_or(bits_count: list[int]) -> int:
            combined_or = 0
            for index in range(32):
                if bits_count[index] > 0:
                    combined_or |= 1 << index
            return combined_or

        length = len(nums)
        bit_frequency = [0] * 32
        current_or_value = 0
        window_start = 0
        shortest_subarray = float('inf')

        for window_end in range(length):
            adjust_count(bit_frequency, nums[window_end], 1)
            current_or_value |= nums[window_end]

            while current_or_value >= k and window_start <= window_end:
                shortest_subarray = min(shortest_subarray, window_end - window_start + 1)
                adjust_count(bit_frequency, nums[window_start], -1)
                current_or_value = calculate_or(bit_frequency)
                window_start += 1

        return -1 if shortest_subarray == float('inf') else shortest_subarray