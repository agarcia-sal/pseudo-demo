class Solution:
    def maxScore(self, nums):
        length_value = len(nums)
        dp_array = [0] * length_value
        index_i = length_value - 2
        while index_i >= 0:
            current_max = 0
            index_j = index_i + 1
            while index_j < length_value:
                partial_score = (index_j - index_i) * nums[index_j]
                combined_score = partial_score + dp_array[index_j]
                if combined_score > current_max:
                    current_max = combined_score
                index_j += 1
            dp_array[index_i] = current_max
            index_i -= 1
        return dp_array[0]