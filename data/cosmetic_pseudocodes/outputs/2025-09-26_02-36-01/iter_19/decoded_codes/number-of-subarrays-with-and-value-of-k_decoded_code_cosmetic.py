from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        length_of_list = len(nums)
        tally = 0

        for index_start in range(length_of_list):
            bitwise_result = nums[index_start]
            pointer_end = index_start
            flag_terminate = False

            while not flag_terminate and pointer_end < length_of_list:
                bitwise_result &= nums[pointer_end]

                if bitwise_result == k:
                    tally += 1

                if bitwise_result < k:
                    flag_terminate = True

                pointer_end += 1

        return tally