class Solution:
    def maximumPrimeDifference(self, nums):
        prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                         59, 61, 67, 71, 73, 79, 83, 89, 97}

        alpha = -1
        omega = -1

        for index, current_element in enumerate(nums):
            if current_element in prime_numbers:
                if alpha == -1:
                    alpha = index
                omega = index

        return omega - alpha