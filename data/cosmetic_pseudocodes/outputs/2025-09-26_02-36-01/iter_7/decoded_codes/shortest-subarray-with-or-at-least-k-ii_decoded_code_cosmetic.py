class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        def update_count(count: list[int], num: int, add: int):
            bit_flag = 1
            index_counter = 0
            # Update count of bits for current num
            while index_counter <= 31:
                if (num & bit_flag) != 0:
                    count[index_counter] += add
                bit_flag <<= 1
                index_counter += 1

        def compute_current_or(count: list[int]) -> int:
            assembled_or = 0
            position = 0
            # Reconstruct OR value from bit counts
            while position <= 31:
                if count[position] > 0:
                    assembled_or |= (1 << position)
                position += 1
            return assembled_or

        length_nums = len(nums)
        bit_counts = [0] * 32
        aggregated_or = 0
        left_pointer = 0
        minimal_length = float('inf')

        right_pointer = 0
        while right_pointer < length_nums:
            update_count(bit_counts, nums[right_pointer], 1)
            aggregated_or |= nums[right_pointer]

            while aggregated_or >= k and left_pointer <= right_pointer:
                current_length = right_pointer - left_pointer + 1
                if minimal_length > current_length:
                    minimal_length = current_length
                update_count(bit_counts, nums[left_pointer], -1)
                aggregated_or = compute_current_or(bit_counts)
                left_pointer += 1

            right_pointer += 1

        return -1 if minimal_length == float('inf') else minimal_length