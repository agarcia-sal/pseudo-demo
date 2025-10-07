class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        def get_relationship(num1, num2):
            if num1 < num2:
                return 1
            elif num1 == num2:
                return 0
            else:
                return -1

        n = len(nums)
        m = len(pattern)
        count = 0

        relationships = []
        for i in range(n - 1):
            relationships.append(get_relationship(nums[i], nums[i + 1]))

        for i in range(n - m):
            if relationships[i:i + m] == pattern:
                count += 1

        return count