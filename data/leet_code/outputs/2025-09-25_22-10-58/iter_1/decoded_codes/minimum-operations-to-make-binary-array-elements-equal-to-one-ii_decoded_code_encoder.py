class Solution:
    def minOperations(self, nums):
        operations = 0
        flip = 0
        for num in nums:
            current_num = num if flip % 2 == 0 else 1 - num
            if current_num == 0:
                operations += 1
                flip += 1
        return operations