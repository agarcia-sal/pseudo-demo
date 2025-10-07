class Solution:
    def maxOperations(self, nums):
        def dfs(leftIdx, rightIdx, targetSum, cache):
            if not (leftIdx < rightIdx):
                return 0

            key = (leftIdx, rightIdx, targetSum)
            if key in cache:
                return cache[key]

            result = 0
            if leftIdx + 1 <= rightIdx and nums[leftIdx] + nums[leftIdx + 1] == targetSum:
                candidate1 = 1 + dfs(leftIdx + 2, rightIdx, targetSum, cache)
                if candidate1 > result:
                    result = candidate1

            if rightIdx - 1 >= leftIdx and nums[rightIdx] + nums[rightIdx - 1] == targetSum:
                candidate2 = 1 + dfs(leftIdx, rightIdx - 2, targetSum, cache)
                if candidate2 > result:
                    result = candidate2

            if nums[leftIdx] + nums[rightIdx] == targetSum:
                candidate3 = 1 + dfs(leftIdx + 1, rightIdx - 1, targetSum, cache)
                if candidate3 > result:
                    result = candidate3

            cache[key] = result
            return result

        n = len(nums)
        if n < 2:
            return 0

        firstCall = 1 + dfs(2, n - 1, nums[0] + nums[1], {})
        secondCall = 1 + dfs(0, n - 3, nums[n - 2] + nums[n - 1], {})
        thirdCall = 1 + dfs(1, n - 2, nums[0] + nums[n - 1], {})

        maxResult = firstCall
        if secondCall > maxResult:
            maxResult = secondCall
        if thirdCall > maxResult:
            maxResult = thirdCall

        return maxResult