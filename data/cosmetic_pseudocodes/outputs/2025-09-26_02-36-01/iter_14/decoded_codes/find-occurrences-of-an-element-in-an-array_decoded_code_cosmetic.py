class Solution:
    def occurrencesOfElement(self, nums, queries, x):
        result = []
        for i, num in enumerate(nums):
            if num == x:
                result.append(i)
        output = []
        for q in queries:
            if q <= len(result):
                output.append(result[q - 1])
            else:
                output.append(0)
        return output