class Solution:
    def maxTotalReward(self, rewardValues):
        rewardValues.sort()

        def dfs(y):
            def bisectRight(arr, target, low, high):
                if low >= high:
                    return low
                mid = (low + high) // 2
                if target <= arr[mid]:
                    return bisectRight(arr, target, mid + 1, high)
                else:
                    return bisectRight(arr, target, low, mid)

            insertionIndex = bisectRight(rewardValues, y, 0, len(rewardValues))

            def iterateFrom(idx, currentMax):
                if idx >= len(rewardValues):
                    return currentMax
                val = rewardValues[idx]
                sumXY = y + val
                updatedMax = currentMax
                if sumXY > y:
                    recResult = dfs(sumXY)
                    candidate = val + recResult
                    if candidate > updatedMax:
                        updatedMax = candidate
                return iterateFrom(idx + 1, updatedMax)

            return iterateFrom(insertionIndex, 0)

        return dfs(0)