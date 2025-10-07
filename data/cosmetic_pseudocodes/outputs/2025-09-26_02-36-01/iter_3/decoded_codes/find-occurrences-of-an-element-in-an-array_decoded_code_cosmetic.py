class Solution:
    def occurrencesOfElement(self, nums, queries, x):
        positions = []
        idx = 0
        while idx < len(nums):
            val = nums[idx]
            if val == x:
                positions.append(idx)
            idx += 1
        results = []
        qIndex = 0
        while qIndex < len(queries):
            req = queries[qIndex]
            if req <= len(positions):
                elementIndex = req - 1
                results.append(positions[elementIndex])
            else:
                results.append(-1)
            qIndex += 1
        return results