class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        length_nums = len(nums)
        length_pattern = len(pattern)
        accumulator = 0
        outer_index = 0

        # Iterate while there is enough room for pattern + 1 elements in nums
        while outer_index <= length_nums - length_pattern - 1:
            verification_flag = True
            inner_idx = 0

            # Check pattern conditions for each position
            while inner_idx < length_pattern:
                left_elem = nums[outer_index + inner_idx]
                right_elem = nums[outer_index + inner_idx + 1]
                current_pattern_elem = pattern[inner_idx]

                if current_pattern_elem == 1:
                    if right_elem <= left_elem:
                        verification_flag = False
                        break
                elif current_pattern_elem == 0:
                    if right_elem != left_elem:
                        verification_flag = False
                        break
                elif current_pattern_elem == -1:
                    if right_elem >= left_elem:
                        verification_flag = False
                        break
                inner_idx += 1

            if verification_flag:
                accumulator += 1
            outer_index += 1

        return accumulator