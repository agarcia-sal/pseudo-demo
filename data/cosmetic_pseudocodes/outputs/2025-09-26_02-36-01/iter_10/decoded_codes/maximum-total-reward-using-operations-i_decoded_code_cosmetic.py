class Solution:
    def maxTotalReward(self, rewardValues):
        def hunt(z):
            def seekInsertPos(arr, target):
                low, high = 0, len(arr)
                while low < high:
                    mid = (low + high) // 2
                    if arr[mid] <= target:
                        low = mid + 1
                    else:
                        high = mid
                return low

            pos = seekInsertPos(rewardValues, z)
            cumulativeMax = 0
            while pos < len(rewardValues):
                val = rewardValues[pos]
                if z + val > z:
                    recursiveResult = hunt(z + val)
                    candidate = val + recursiveResult
                    if candidate > cumulativeMax:
                        cumulativeMax = candidate
                pos += 1
            return cumulativeMax

        n = len(rewardValues)
        idx = 1
        while idx < n:
            key = rewardValues[idx]
            inner = idx - 1
            while inner >= 0 and rewardValues[inner] > key:
                rewardValues[inner + 1] = rewardValues[inner]
                inner -= 1
            rewardValues[inner + 1] = key
            idx += 1

        return hunt(0)