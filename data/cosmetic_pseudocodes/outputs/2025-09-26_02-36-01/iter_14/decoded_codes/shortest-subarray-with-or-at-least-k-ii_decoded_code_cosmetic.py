from math import inf

class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        def adjust_frequency(freq: list[int], val: int, delta: int) -> None:
            bitmask = 1
            index = 0
            while index < 32:
                if val & bitmask != 0:
                    freq[index] += delta
                bitmask <<= 1
                index += 1

        def calculate_or(freq: list[int]) -> int:
            accumulator = 0
            position = 0
            while position < 32:
                if freq[position] > 0:
                    accumulator |= (1 << position)
                position += 1
            return accumulator

        length_nums = len(nums)
        frequencies = [0] * 32
        combined_or = 0
        start_pointer = 0
        smallest_len = inf

        end_pointer = 0
        while end_pointer < length_nums:
            adjust_frequency(frequencies, nums[end_pointer], 1)
            combined_or |= nums[end_pointer]

            while combined_or >= k and start_pointer <= end_pointer:
                current_len = end_pointer - start_pointer + 1
                if smallest_len > current_len:
                    smallest_len = current_len
                adjust_frequency(frequencies, nums[start_pointer], -1)
                combined_or = calculate_or(frequencies)
                start_pointer += 1

            end_pointer += 1

        return -1 if smallest_len == inf else smallest_len