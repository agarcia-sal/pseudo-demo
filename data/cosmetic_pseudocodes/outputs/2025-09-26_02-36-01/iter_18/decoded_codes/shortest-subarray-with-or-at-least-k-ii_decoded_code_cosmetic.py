class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        def delta_update(freq: list[int], val: int, delta: int) -> None:
            bit_flag = 1
            idx = 0
            while idx < 32:
                if (val & bit_flag) != 0:
                    freq[idx] += delta
                bit_flag <<= 1
                idx += 1

        def aggregate_or(freq: list[int]) -> int:
            acc = 0
            pos = 0
            while pos < 32:
                if freq[pos] > 0:
                    acc |= (1 << pos)
                pos += 1
            return acc

        length_nums = len(nums)
        counts = [0] * 32
        or_value = 0
        start_idx = 0
        best_len = float('inf')

        end_idx = 0
        while end_idx < length_nums:
            delta_update(counts, nums[end_idx], 1)
            or_value |= nums[end_idx]

            while or_value >= k and start_idx <= end_idx:
                current_len = end_idx - start_idx + 1
                if best_len > current_len:
                    best_len = current_len
                delta_update(counts, nums[start_idx], -1)
                or_value = aggregate_or(counts)
                start_idx += 1

            end_idx += 1

        return -1 if best_len == float('inf') else best_len