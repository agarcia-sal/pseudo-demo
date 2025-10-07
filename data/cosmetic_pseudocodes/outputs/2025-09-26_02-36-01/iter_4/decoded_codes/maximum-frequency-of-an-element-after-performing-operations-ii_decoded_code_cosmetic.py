from collections import defaultdict

class Solution:
    def maxFrequency(self, nums, k, numOperations):
        frequencyMap = defaultdict(int)
        diffMap = defaultdict(int)

        currentIndex = 0
        while currentIndex < len(nums):
            num = nums[currentIndex]
            frequencyMap[num] += 1
            diffMap[num] += 0  # ensure key exists
            diffMap[num - k] += 1
            diffMap[num + k + 1] -= 1
            currentIndex += 1

        maxCount = 0
        cumulativeSum = 0
        sortedKeysList = sorted(diffMap.keys())

        position = 0
        while position < len(sortedKeysList):
            keyValue = sortedKeysList[position]
            incrementVal = diffMap[keyValue]
            cumulativeSum += incrementVal
            tempVal = min(cumulativeSum, frequencyMap[keyValue] + numOperations)
            if tempVal > maxCount:
                maxCount = tempVal
            position += 1

        return maxCount