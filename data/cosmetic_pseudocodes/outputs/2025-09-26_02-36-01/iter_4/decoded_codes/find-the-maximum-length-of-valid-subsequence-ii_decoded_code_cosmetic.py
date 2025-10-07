class Solution:
    def maximumLength(self, nums, k):
        total_elements = len(nums)
        if total_elements == 1:
            return 1

        dp_list = [{} for _ in range(total_elements)]
        longest_seq = 1

        for outer_index in range(total_elements):
            for inner_index in range(outer_index):
                current_sum = nums[outer_index] + nums[inner_index]
                remainder_val = current_sum % k

                if remainder_val in dp_list[inner_index]:
                    dp_list[outer_index][remainder_val] = dp_list[inner_index][remainder_val] + 1
                else:
                    dp_list[outer_index][remainder_val] = 2

                if dp_list[outer_index][remainder_val] > longest_seq:
                    longest_seq = dp_list[outer_index][remainder_val]

        return longest_seq