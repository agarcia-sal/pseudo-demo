class Solution:
    def maxOperations(self, nums):
        def dfs(leftIndex, rightIndex, targetScore, cache):
            if leftIndex >= rightIndex:
                return 0
            if (leftIndex, rightIndex, targetScore) in cache:
                return cache[(leftIndex, rightIndex, targetScore)]
            result = 0

            # Check if the sum of nums[leftIndex] and nums[leftIndex + 1] equals targetScore
            if leftIndex + 1 <= rightIndex and nums[leftIndex] + nums[leftIndex + 1] == targetScore:
                candidate = 1 + dfs(leftIndex + 2, rightIndex, targetScore, cache)
                if candidate > result:
                    result = candidate

            # Check if the sum of nums[rightIndex] and nums[rightIndex - 1] equals targetScore
            if rightIndex - 1 >= leftIndex and nums[rightIndex] + nums[rightIndex - 1] == targetScore:
                candidate = 1 + dfs(leftIndex, rightIndex - 2, targetScore, cache)
                if candidate > result:
                    result = candidate

            # Check if the sum of nums[leftIndex] and nums[rightIndex] equals targetScore
            if nums[leftIndex] + nums[rightIndex] == targetScore:
                candidate = 1 + dfs(leftIndex + 1, rightIndex - 1, targetScore, cache)
                if candidate > result:
                    result = candidate

            cache[(leftIndex, rightIndex, targetScore)] = result
            return result

        totalLength = len(nums)

        # Guard against small input lengths to avoid index errors
        if totalLength < 2:
            return 0
        cache = {}

        optionOne = 1 + dfs(2, totalLength - 1, nums[0] + nums[1], cache) if totalLength > 2 else 1
        cache.clear()
        optionTwo = 1 + dfs(0, totalLength - 4, nums[totalLength - 2] + nums[totalLength - 1], cache) if totalLength > 4 else 1
        cache.clear()
        optionThree = 1 + dfs(1, totalLength - 2, nums[0] + nums[totalLength - 1], cache) if totalLength > 2 else 1

        resultList = [optionOne, optionTwo, optionThree]
        maxResult = resultList[0]
        i = 1
        while i < len(resultList):
            if resultList[i] > maxResult:
                maxResult = resultList[i]
            i += 1

        return maxResult