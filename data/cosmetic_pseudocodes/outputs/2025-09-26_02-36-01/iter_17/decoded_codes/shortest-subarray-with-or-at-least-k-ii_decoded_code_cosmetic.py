class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:

        def update_count(hist: list[int], val: int, inc: int) -> None:
            bit = 1
            idx = 0
            while idx < 32:
                if (val & bit) != 0:
                    hist[idx] += inc
                bit <<= 1
                idx += 1

        def compute_current_or(hist: list[int]) -> int:
            acc = 0
            pos = 0
            while pos < 32:
                if hist[pos] > 0:
                    acc |= (1 << pos)
                pos += 1
            return acc

        length_nums = len(nums)
        frequencies = [0] * 32
        or_value = 0
        start_idx = 0
        min_len = float('inf')

        current_idx = 0
        while current_idx < length_nums:
            update_count(frequencies, nums[current_idx], 1)
            or_value |= nums[current_idx]

            while or_value >= k and start_idx <= current_idx:
                if min_len > (current_idx - start_idx + 1):
                    min_len = current_idx - start_idx + 1
                update_count(frequencies, nums[start_idx], -1)
                or_value = compute_current_or(frequencies)
                start_idx += 1

            current_idx += 1

        return -1 if min_len == float('inf') else min_len