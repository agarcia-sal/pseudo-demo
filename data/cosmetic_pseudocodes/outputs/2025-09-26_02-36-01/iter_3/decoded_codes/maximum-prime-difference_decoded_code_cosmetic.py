class Solution:
    def maximumPrimeDifference(self, nums):
        prime_collection = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                            53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
        initial_position = -1
        final_position = -1
        counter = 0
        while counter < len(nums):
            element = nums[counter]
            if element in prime_collection:
                if initial_position < 0:
                    initial_position = counter
                final_position = counter
            counter += 1
        return final_position - initial_position