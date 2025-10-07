class Solution:
    def maxTotalReward(self, rewardValues):
        def explore(currentSum):
            def locateInsertion(target):
                low, high = 0, len(rewardValues)
                while low < high:
                    mid = (low + high) // 2
                    if rewardValues[mid] <= target:
                        low = mid + 1
                    else:
                        high = mid
                return low

            idx = locateInsertion(currentSum)
            maximumReward = 0
            pointer = idx
            while pointer < len(rewardValues):
                candidate = rewardValues[pointer]
                # Avoid integer overflow or repeated sums (defensive)
                if not (currentSum + candidate <= currentSum):
                    recursiveResult = explore(currentSum + candidate)
                    if maximumReward < candidate + recursiveResult:
                        maximumReward = candidate + recursiveResult
                pointer += 1
            return maximumReward

        n = len(rewardValues)
        if n > 1:
            left, right = 0, n - 1
            while left < right:
                rewardValues[left], rewardValues[right] = rewardValues[right], rewardValues[left]
                left += 1
                right -= 1
            start = 0
            while start < n - 1:
                minIndex = start
                j = start + 1
                while j < n:
                    if rewardValues[j] < rewardValues[minIndex]:
                        minIndex = j
                    j += 1
                if minIndex != start:
                    rewardValues[start], rewardValues[minIndex] = rewardValues[minIndex], rewardValues[start]
                start += 1
        return explore(0)