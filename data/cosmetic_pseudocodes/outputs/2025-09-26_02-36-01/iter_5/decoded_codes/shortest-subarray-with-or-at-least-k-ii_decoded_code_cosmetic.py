class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:

        def update_count(count: list[int], num: int, add: int) -> None:
            def loop_bits(position: int, mask_val: int) -> None:
                if position == 32:
                    return
                if (num & mask_val) != 0:
                    count[position] += add
                loop_bits(position + 1, mask_val << 1)

            loop_bits(0, 1)

        def compute_current_or(count: list[int]) -> int:
            def loop_or(index: int, acc: int) -> int:
                if index == 32:
                    return acc
                if count[index] > 0:
                    acc |= (1 << index)
                return loop_or(index + 1, acc)

            return loop_or(0, 0)

        len_nums = len(nums)
        bit_counts = [0] * 32
        combined_or = 0
        start_idx = 0
        shortest_len = float('inf')

        def while_loop():
            nonlocal combined_or, start_idx, shortest_len
            while combined_or >= k and start_idx <= end_idx:
                current_len = end_idx - start_idx + 1
                if shortest_len > current_len:
                    shortest_len = current_len
                update_count(bit_counts, nums[start_idx], -1)
                combined_or = compute_current_or(bit_counts)
                start_idx += 1

        end_idx = 0
        while end_idx < len_nums:
            update_count(bit_counts, nums[end_idx], 1)
            combined_or |= nums[end_idx]
            while_loop()
            end_idx += 1

        return -1 if shortest_len == float('inf') else shortest_len