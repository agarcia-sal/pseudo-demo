class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        def update_count(cnt: list[int], val: int, delta: int) -> None:
            bit_mask = 1
            idx = 0
            while idx < 32:
                if val & bit_mask != 0:
                    cnt[idx] += delta
                bit_mask <<= 1
                idx += 1

        def compute_current_or(cnt: list[int]) -> int:
            result = 0
            pos = 0
            while pos < 32:
                if cnt[pos] > 0:
                    result |= (1 << pos)
                pos += 1
            return result

        length_nums = len(nums)
        counts = [0] * 32

        curr_or = 0
        l_ptr = 0
        minimal_len = float('inf')

        for r_ptr in range(length_nums):
            update_count(counts, nums[r_ptr], 1)
            curr_or |= nums[r_ptr]

            while curr_or >= k and l_ptr <= r_ptr:
                current_len = r_ptr - l_ptr + 1
                if minimal_len > current_len:
                    minimal_len = current_len
                update_count(counts, nums[l_ptr], -1)
                curr_or = compute_current_or(counts)
                l_ptr += 1

        return -1 if minimal_len == float('inf') else minimal_len